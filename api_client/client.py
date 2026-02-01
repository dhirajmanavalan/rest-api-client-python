import requests
from config import BASE_URL, HEADERS
from exceptions import NetworkError, TimeoutError

def _handle_request(method, url, **kwargs):
    try:
        response = requests.request(method , url , headers=HEADERS, timeout=3, **kwargs)
        return response
    except requests.exceptions.Timeout:
        raise TimeoutError("Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        raise NetworkError("Network error. Check your internet connection.")
    except requests.exceptions.RequestException:
        raise NetworkError("Unexpected network error occurred.")

def get_all_posts():
    return _handle_request('GET', f'{BASE_URL}/posts')

def get_post_id(post_id):
    return _handle_request('GET', f'{BASE_URL}/posts/{post_id}')

def create_post(data):
    return _handle_request('POST', f'{BASE_URL}/posts', json = data)

def update_post(post_id, data):
    return _handle_request('PUT', f'{BASE_URL}/posts/{post_id}', json = data)


def delete_post(post_id):
    return _handle_request('DELETE', f'{BASE_URL}/posts/{post_id}',)