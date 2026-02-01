import requests

from config import BASE_URL, HEADERS

def get_all_posts():
    return requests.get(f"{BASE_URL}/posts", headers=HEADERS, timeout=3)

def get_post_id(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}", headers=HEADERS, timeout=3)

def create_post(data):
    return requests.post(f"{BASE_URL}/posts", json=data, headers=HEADERS, timeout=3)

def update_post(post_id, data):
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=data, headers=HEADERS, timeout=3)


def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}", headers=HEADERS, timeout=3)