from requests_books.api_clients import *

class TestApiClient:
    nr = randint(1,9999999)
    clientName = 'Teo'
    clientEmail = f'valid_email{nr}@mailinator.com'

    def setup_method(self):
        self.response =login(self.clientName, self.clientEmail)

    def test_successful_login(self):
        assert self.response.status_code == 201, 'Actual code is not correct.'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in response keys.'

    def test_login_client_already_registered(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'

    def test_invalid_email(self):
        self.response = login('def','abc')
        assert self.response.status_code == 400
        assert self.response.json()['error'] == 'Invalid or missing client email.'


