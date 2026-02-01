from client import (
    get_all_posts,
    get_post_id,
    create_post,
    update_post,
    delete_post
)

def validate_post_data(title: str , body: str):
    if not title or not title.strip():
        return False, 'Title Cannot be Empty'
    
    if not body or not body.strip():
        return False, 'Body cannot be Empty'
    
    return True, None

def fetch_all_posts():
    response = get_all_posts()
    if response.status_code == 200:
        posts = response.json()
        return posts[:3]
    return None

def fetch_posts_by_id(post_id : int):
    response = get_post_id(post_id)
    if response.status_code == 200:
        return response.json()
    return None

def create_post_service(title : str , body : str):
    is_valid , error = validate_post_data(title,body)
    if not is_valid:
        return {'error':error}
    
    payload = {
        'title' : title,
        'body' : body,
        'userId' : 1
    }
    
    response = create_post(payload)
    
    if response.status_code == 201:
        return response.json()
    return {'error' : 'failed to create post'}

def update_post_service(post_id: int, title : str, body : str):
    is_valid, error = validate_post_data(title, body)
    if not is_valid:
        return {"error": error}

    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }

    response = update_post(post_id, payload)
    if response.status_code == 200:
        return response.json()

    return {"error": "Failed to update post"}

def delete_post_service(post_id : int):
    response = delete_post(post_id)
    if response.status_code == 200:
        return True
    return False

    
