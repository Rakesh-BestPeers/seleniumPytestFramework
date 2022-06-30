import requests
from requests.auth import HTTPBasicAuth


class Main:
    def __init__(self):
        pass

    def auth_post(self):
        self.url = "https://node-fake-api-server.herokuapp.com/user"
        self.payload = {"external_id": "postman"}
        self.headers = {
            'Content-Type': "application/json,text/plain",
            'X-FakeAPI-Action': 'register'}

        response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
        print(response.text)
        print(response.status_code)

        data = response.json()
        username = data['username']
        print(username)
        password = data['password']
        print(password)


    def auth_get(self, username, password):
        url_put = "https://node-fake-api-server.herokuapp.com/"
        auth = HTTPBasicAuth('username', 'password')
        body = {
            "method": "get",
            "path": "/hello-world",
            "query_parameters": {
                "who": "bar"
            },
            "responses": [
                {
                    "status": 200,
                    "content": "Hello bar!",
                    "content_type": "text/plain"
                }
            ]
        }
        header1 = {
            'Content-Type': "application/json,text/plain",
            'X-FakeAPI-Action': 'record'}
        response = requests.request("PUT", url_put, data=body, headers=header1, auth=auth)
        print(response.text)
        print(response.status_code)

        return response

object = Main()
obj=object.auth_post()
print("return value is ", object)
obj=object.auth_get()