from client import (
    get_all_posts,
    get_post_id,
    create_post,
    update_post,
    delete_post
)

from exceptions import(
    BadRequestError,
    UnauthorizedError,
    NotFoundError,
    ServerError,
    
    MethodNotAllowedError
)

def _handle_status(response):
    if response.status_code in (200, 201):
        return
    if response.status_code == 400:
        raise BadRequestError("Bad request. Please check input.")
    if response.status_code == 401:
        raise UnauthorizedError("Unauthorized. Check API key.")
    if response.status_code == 404:
        raise NotFoundError("Resource not found.")
    if response.status_code >= 500:
        raise ServerError("Server error. Try later.")
    
    raise ServerError(f"Unexpected server response (status code: {response.status_code})")

def validate_post_data(title: str , body: str):
    if not title or not title.strip():
        return False, 'Title Cannot be Empty'
    
    if not body or not body.strip():
        return False, 'Body cannot be Empty'
    
    return True, None

def fetch_all_posts():
    response = get_all_posts()
    _handle_status(response)
    
    try:
        return response.json()
    
    except ValueError:
        raise ServerError("Invalid JSON response from server.")
    
def fetch_posts_by_id(post_id: int):
    response = get_post_id(post_id)
    _handle_status(response)
    return response.json()

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
    
    _handle_status(response)
    return response.json()

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
    _handle_status(response)
    return response.json()

def delete_post_service(post_id : int):
    response = delete_post(post_id)
    _handle_status(response)
    return True

    
