import requests
user_id=int(input("Enter user ID (1-10):"))
try:
    url=f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response=requests.get(url)
    if(response.status_code==200):
        info=response.json()
        print("---USER INFORMATION---")
        print("Name:",info["name"])
        print("Username:",info["username"])
        print("Email:",info["email"])
        print("City:",info["address"]["city"])
        print("Phone:",info["phone"])
        print("Website:",info["website"],"\n")
    else:
        print("User not found")
except requests.exceptions.RequestException:
    print("Request can't be fulfilled")

