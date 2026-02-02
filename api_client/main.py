from services import (
    fetch_all_posts,
    fetch_posts_by_id,
    create_post_service,
    update_post_service,
    delete_post_service
)

from exceptions import APIClientError


while True:
    print("\nChoose an option:")
    print("1. Get all posts")
    print("2. Get post by ID")
    print("3. Create post")
    print("4. Update post")
    print("5. Delete post")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    
    try:

        if choice == "1":
            posts = fetch_all_posts()
            if posts:
                for post in posts:
                    print(f"ID: {post['id']} | Title: {post['title']}")
            else:
                print("Failed to fetch posts")

        elif choice == "2":
            post_id = int(input("Enter post ID: "))
            post = fetch_posts_by_id(post_id)
            if post:
                print(f"\nTitle: {post['title']}")
                print(f"Body: {post['body']}")
            else:
                print("Post not found")

        elif choice == "3":
            title = input("Enter title: ")
            body = input("Enter body: ")
            result = create_post_service(title, body)

            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Post created successfully with ID: {result['id']}")

        elif choice == "4":
            post_id = int(input("Enter post ID: "))
            title = input("Enter title: ")
            body = input("Enter body: ")
            result = update_post_service(post_id, title, body)

            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print("Post updated successfully")

        elif choice == "5":
            post_id = int(input("Enter post ID: "))
            success = delete_post_service(post_id)
            if success:
                print("Post deleted successfully")
            else:
                print("Failed to delete post")

        elif choice == "6":
            print("Exiting application")
            break

        else:
            print("Invalid choice. Try again.")
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        
    except APIClientError as e:
        print(f"{e}")
        
    except Exception:
        print("Unexpected application error. Please try again.")
