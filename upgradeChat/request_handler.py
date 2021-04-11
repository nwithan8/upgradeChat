import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient

from objectrest import requests as objectrest_requests
from upgradeChat import utils


class RequestHandler:
    def __init__(self, base_url: str, client_id: str, client_secret: str):
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        self._base = base_url
        self._id = client_id
        self._secret = client_secret

        self._tokens = self._authorize()
        self._session = requests.Session()

    def _authorize(self):
        """
        Access token seems to be valid for a month
        Refresh token seems to be valid for a year

        :return:
        :rtype:
        """
        url = "https://api.upgrade.chat/oauth/token"
        auth = HTTPBasicAuth(self._id, self._secret)
        client = BackendApplicationClient(client_id=self._id)
        oauth = OAuth2Session(client=client)
        return oauth.fetch_token(token_url=url, auth=auth)

    def _get_access_token(self):
        """
        Handle refreshing tokens if needed

        :return:
        :rtype:
        """
        # If not authorized already
        if not self._tokens:
            self._authorize()

        # If access token has expired
        access_token_expiration_timestamp = self._tokens.get('access_token_expires_in')
        if not access_token_expiration_timestamp \
                or utils.timestamp_is_expired(timestamp=access_token_expiration_timestamp):
            self._authorize()

        if not self._tokens:
            raise Exception("Could not get tokens from the API.")

        access_token = self._tokens.get('access_token')
        if not access_token:
            raise Exception("No access token provided by the API.")
        return access_token

    def _get_headers(self):
        access_token = self._get_access_token()
        return {'Authorization': f'Bearer {access_token}'}

    def _make_url(self, uri: str):
        if uri.startswith("/"):
            uri = uri[1:]
        return f"{self._base}/{uri}"

    def get_json(self, uri: str, params: dict = None):
        """
        Get API response as JSON

        :param uri:
        :type uri:
        :param params:
        :type params:
        :return:
        :rtype:
        """
        url = self._make_url(uri)
        headers = self._get_headers()
        return objectrest_requests.get_json(url=url, session=self._session, params=params, headers=headers)

    def get_object(self, uri: str, model: type, params: dict = None):
        """
        Get API response as an object

        :param uri:
        :type uri:
        :param params:
        :type params:
        :return:
        :rtype:
        """
        url = self._make_url(uri)
        headers = self._get_headers()
        return objectrest_requests.get_object(url=url, model=model, session=self._session, params=params, headers=headers)
