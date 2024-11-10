from flask import Response, json

'''
    Builder creational design pattern used
    to build the Flask Response object to the client  
'''

class ApiResponseBuilder:
    def __init__(self):
        self._status_code = 200
        self._headers = {}
        self._response = {}
        self._content_type = 'application/json'

    def add_data(self, data):
        self._response['data'] = data
        return self

    def set_success(self, success: int):
        self._response['success'] = success
        return self

    def add_info(self, typ: str, message: str):
        if 'information' not in self._response:
            self._response['information'] = {}

        if typ not in self._response['information']:
            self._response['information'][typ] = []

        self._response['information'][typ].append(message)
        return self

    def set_status_code(self, status):
        self._status_code = status
        return self

    def set_content_type(self, content_type):
        self._content_type = content_type
        return self

    def set_header(self, header, value):
        self._headers[header] = value
        return self

    def build(self):
        response_body = json.dumps(self._response)
        response = Response(
            response=response_body,
            status=self._status_code,
            headers=self._headers,
            content_type=self._content_type
        )
        return response
