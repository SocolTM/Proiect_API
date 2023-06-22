from requests_books.status import*

class TestStatus:

    def test_status_code(self):
        s_code = get_status().status_code
        assert s_code == 200, f'Status code is incorrect.' \
                              f'Expected code is status 200, but the actual is {s_code}'

    def test_body_result(self):
        result = get_status().json()
        print(result)
        #['status']
        #
        #assert result == "ok", f'The status value is not ok. Actual: {result}'
