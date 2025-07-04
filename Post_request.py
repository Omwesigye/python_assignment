import requests


url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'My Test',
    'body': 'This is a body',
    'userId': 1
}


response = requests.post(url, json=data)


print("Status Code:", response.status_code)
print("Response JSON:", response.json())
