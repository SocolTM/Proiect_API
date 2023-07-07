import requests
from requests.structures import CaseInsensitiveDict
def __setHeaders(token):
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    return headers

def add_order(token, bookId, customerName):
    headers = __setHeaders(token)
    json = {
        'bookId': bookId,
        'customerName': customerName
    }
    response = requests.post(f'https://simple-books-api.glitch.me/orders', headers=headers, json=json)
    return response

def delete_order(token, orderId):
    headers = __setHeaders(token)
    response = requests.delete(f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers)
    return response

def get_orders(token):
    headers = __setHeaders(token)
    response = requests.get(f'https://simple-books-api.glitch.me/orders', headers=headers)
    return response

def get_order(token, orderId):
    headers = __setHeaders(token)
    response = requests.get(f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers)
    return response

def edit_order(token, bookId, customerName):
    headers = __setHeaders(token)
    json = {
        'customerName': customerName
    }
    response = requests.patch(f'https://simple-books-api.glitch.me/orders/{bookId}', headers=headers, json=json)
    return response