import requests


def authpostAPI(self):
    self.url = "https://node-fake-api-server.herokuapp.com/user"
    self.payload = {"external_id": "postman"}
    headers = {
        'Content-Type': "application/json,text/plain",
        'X-FakeAPI-Action': 'register',
    }
    response = requests.request("POST", self.url, data=self.payload, headers=headers)
    print(response.text)
    data = response.json()
    username = data['username']
    print(username)
    password = data['password']
    print(password)
