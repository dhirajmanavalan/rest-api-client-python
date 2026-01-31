import requests

from config import BASE_URL, HEADERS

def get_all_posts():
    url = f'{BASE_URL}/posts'
    response = requests.get(url,headers=HEADERS, timeout=3)
    return response

def get_post_id(post_id):
    url = f'{BASE_URL}/posts/{post_id}'
    response = requests.get(url, headers=HEADERS, timeout=3)
    return response

def create_post(data):
    url = f"{BASE_URL}/posts"
    response = requests.post(url, json=data, headers=HEADERS, timeout=3)
    return response

def update_post(post_id, data):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.put(url, json=data, headers=HEADERS, timeout=3)
    return response


def delete_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.delete(url, headers=HEADERS, timeout=3)
    return response

if __name__ == '__main__':

    while True:
        print("\nChoose an option:")
        print("1. Get all posts")
        print("2. Get post by ID")
        print("3. Create post")
        print("4. Update post")
        print("5. Delete post")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            res = get_all_posts()
            print(res.status_code)
            print(res.json()[:2])

        elif choice == "2":
            post_id = int(input("Enter post id: "))
            res = get_post_id(post_id)
            print(res.status_code)
            print(res.json())

        elif choice == "3":
            data = {
                "title": input("Enter title: "),
                "body": input("Enter body: "),
                "userId": 1
            }
            res = create_post(data)
            print(res.status_code)
            print(res.json())

        elif choice == "4":
            post_id = int(input("Enter post id: "))
            data = {
                "title": input("Enter title: "),
                "body": input("Enter body: "),
                "userId": 1
            }
            res = update_post(post_id, data)
            print(res.status_code)
            print(res.json())

        elif choice == "5":
            post_id = int(input("Enter post id: "))
            res = delete_post(post_id)
            print(res.status_code)
            print("Post deleted")

        elif choice == "6":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Try again.")