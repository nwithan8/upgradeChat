import time

def timestamp_is_expired(timestamp: str):
    try:
        timestamp = int(timestamp)
        current_timestamp = int(time.time())
        return timestamp < current_timestamp
    except:
        raise Exception("Could not check timestamp expiration.")