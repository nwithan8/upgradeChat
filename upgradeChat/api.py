from typing import Union

from objectrest import OAuth2RequestHandler

from upgradeChat.models import *


# TODO: __str__ for all model objects and sub-objects

class API:
    def __init__(self, client_id: str, client_secret: str, raw: bool = False):
        self._make_objects = not raw
        self._request_handler = OAuth2RequestHandler(client_id=client_id,
                                                     client_secret=client_secret,
                                                     authorization_url="https://api.upgrade.chat/oauth/token",
                                                     base_url="https://api.upgrade.chat/v1")

    def _request(self, uri: str, params: dict = None, model: type = None) -> Union[object, dict]:
        if self._make_objects:
            return self._request_handler.get_object(url=uri, model=model, params=params)
        return self._request_handler.get_json(url=uri, params=params)

    # Orders
    def get_orders(self, order_type: str = None, discord_id: int = None, limit: int = 100, offset: int = 0) -> Union[
        Orders, dict]:
        """
        Get a list of orders

        :param order_type: filter to a specific order type
        :type order_type: str
        :param discord_id: filter to a specific Discord user
        :type discord_id: int
        :param limit: limit the number of items returned (default: 100)
        :type limit: int
        :param offset: offset the number of items returned (default: 0)
        :type offset: int
        :return: Orders object or JSON
        :rtype: Orders | dict
        """
        params = {
            'limit': limit,
            'offset': offset,
        }
        if discord_id:
            params['userDiscordId'] = discord_id
        if order_type:
            params['type'] = order_type
        return self._request(uri='orders', params=params, model=Orders)

    @property
    def orders(self) -> Union[Orders, dict]:
        """
        Get all orders (up to 100)

        :return: Orders object or JSON
        :rtype: Orders | dict
        """
        return self.get_orders()

    def orders_for_user(self, discord_id: int) -> Union[Orders, dict]:
        """
        Get a list of orders for a specific Discord user

        :param discord_id: Discord ID of user
        :type discord_id: int
        :return: Orders object or JSON
        :rtype: Orders | dict
        """
        return self.get_orders(discord_id=discord_id)

    def get_order(self, order_id: str) -> Union[Order, dict]:
        """
        Get a specific order

        :param order_id: ID of the order
        :type order_id: str
        :return: Order object or JSON
        :rtype: Order | dict
        """
        return self._request(uri=f"orders/{order_id}", model=Order)

    # Products
    def get_products(self, product_type: str = None, limit: int = 100, offset: int = 0) -> Union[Products, dict]:
        """
        Get a list of products

        :param product_type: filter to a specific product type
        :type product_type: str
        :param limit: limit the number of items returned (default: 100)
        :type limit: int
        :param offset: offset the number of items returned (default: 0)
        :type offset: int
        :return: Products object or JSON
        :rtype: Products | dict
        """
        params = {
            'limit': limit,
            'offset': offset
        }
        if product_type:
            params['type'] = product_type
        return self._request(uri=f"products", params=params, model=Products)

    @property
    def products(self) -> Union[Products, dict]:
        """
        Get all products (up to 100)

        :return: Products object or JSON
        :rtype: Products | dict
        """
        return self.get_products()

    def get_product(self, product_id: str) -> Union[Product, dict]:
        """
        Get a specific product

        :param product_id: ID of the product
        :type product_id: str
        :return: Product object or JSON
        :rtype: Product | dict
        """
        return self._request(uri=f"products/{product_id}", model=Product)

    # Users
    def get_users(self, limit: int = 100, offset: int = 0) -> Union[Users, dict]:
        """
        Get a list of users

        :param limit: limit the number of items returned (default: 100)
        :type limit: int
        :param offset: offset the number of items returned (default: 0)
        :type offset: int
        :return: Users object or JSON
        :rtype: Users | dict
        """
        params = {
            'limit': limit,
            'offset': offset
        }
        return self._request(uri=f"users", params=params, model=Users)

    @property
    def users(self) -> Union[Users, dict]:
        """
        Get all users (up to 100)

        :return: Users object or JSON
        :rtype: Users | dict
        """
        return self.get_users()

    # Webhooks
    def get_webhooks(self, limit: int = 100, offset: int = 0) -> Union[Webhooks, dict]:
        """
        Get a list of webhooks

        :param limit: limit the number of items returned (default: 100)
        :type limit: int
        :param offset: offset the number of items returned (default: 0)
        :type offset: int
        :return: Webhooks object or JSON
        :rtype: Webhooks | dict
        """
        params = {
            'limit': limit,
            'offset': offset
        }
        return self._request(uri=f"webhooks", params=params, model=Webhooks)

    @property
    def webhooks(self) -> Union[Webhooks, dict]:
        """
        Get all webhooks (up to 100)

        :return: Webhooks object or JSON
        :rtype: Webhooks | dict
        """
        return self.get_webhooks()

    def get_webhook(self, webhook_id: str) -> Union[Webhook, dict]:
        """
        Get a specific webhook

        :param webhook_id: ID of the webhook
        :type webhook_id: str
        :return: Webhook object or JSON
        :rtype: Webhook | dict
        """
        return self._request(uri=f"webhooks/{webhook_id}", model=Webhook)

    # Webhook Events
    def get_webhook_events(self, limit: int = 100, offset: int = 0) -> Union[WebookEvents, dict]:
        """
        Get a list of webhook events

        :param limit: limit the number of items returned (default: 100)
        :type limit: int
        :param offset: offset the number of items returned (default: 0)
        :type offset: int
        :return: WebhookEvents object or JSON
        :rtype: WebhookEvents | dict
        """
        params = {
            'limit': limit,
            'offset': offset
        }
        return self._request(uri=f"webhook-events", params=params, model=WebookEvents)

    @property
    def webhook_events(self) -> Union[WebookEvents, dict]:
        """
        Get all webhook events (up to 100)

        :return: WebhookEvents object or JSON
        :rtype: WebhookEvents | dict
        """
        return self.get_webhook_events()

    def get_webhook_event(self, webhook_event_id: str) -> Union[WebhookEvent, dict]:
        """
        Get a specific webhook event

        :param webhook_event_id: ID of the webhook event
        :type webhook_event_id: str
        :return: WebhookEvent object or JSON
        :rtype: WebhookEvent | dict
        """
        return self._request(uri=f"webhook-events/{webhook_event_id}", model=WebhookEvent)

    def validate_webhook_event(self, webhook_event_id: str) -> bool:
        """
        Validate a webhook event

        :param webhook_event_id: ID of the webhook event
        :type webhook_event_id: str
        :return: True or False
        :rtype: bool
        """
        data = self._request_handler.get_json(uri=f"webhook-events/{webhook_event_id}/validate")
        return data.get('valid', False)
