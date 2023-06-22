from requests_books.api_clients import *
from requests_books.orders import *

class TestOrders:

    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'Teo')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'This book is not in stock. Try again later.'

    def test_add_valid_order(self):
        response = add_order(self.token, 1, 'Teo')
        assert response.status_code == 201
        assert response.json()['created'] is True
        #clean_up
        delete_order(self.token,response.json()['orderId'])

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'user1')
        add2 = add_order(self.token, 1, 'user2')
        response = get_orders(self.token)
        assert response.status_code == 200
        assert len(response.json()) == 2
        #clean_up
        delete_order(self.token,add1.json()['orderId'])
        delete_order(self.token,add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token,1,'user1')
        response = delete_order(self.token,add.json()['orderId'])
        assert response.status_code == 204
        get_all = get_orders(self.token)
        assert len(get_all.json()) == 0

    def test_delete_invalid_order_id(self):
        response = delete_order(self.token, 'z5iZN3No-BVz7J6uzYug899')
        assert response.status_code == 404
        assert response.json()['error'] == 'No order with id z5iZN3No-BVz7J6uzYug899.'

    def test_get_order(self):
        order_id = add_order(self.token, 1, 'user1').json()['orderId']
        response = get_order(self.token,order_id)
        assert response.status_code == 200
        assert response.json()['id'] == order_id
        assert response.json()['bookId'] == 1
        assert response.json()['customerName'] == 'user1'
        assert response.json()['quantity'] == 1
        #clean_up
        delete_order(self.token, order_id)

    def test_get_invalid_order_id(self):
        response = get_order(self.token,'njiyygf')
        assert response.status_code == 404
        assert response.json()['error'] == 'No order with id njiyygf.'

    def test_patch_invalid_order_id(self):
        response = edit_order(self.token, '1234656789','Alex')
        assert response.status_code == 404, ''
        assert response.json()['error'] == 'No order with id 1234656789.'

    def test_patch_valid_order(self):
        order_id = add_order(self.token,1, 'Teo',).json()['orderId']
        response = edit_order(self.token, order_id, 'Teo2')
        assert response.status_code == 204
        get = get_order(self.token, order_id)
        assert get.json()['customerName'] == 'Teo2'
        #clean_up
        delete_order(self.token, order_id)











