import requests
from requests.auth import HTTPDigestAuth
response_data = requests.get('https://httpbin.org/digest-auth/auth/admin/admin123',
auth = HTTPDigestAuth('admin', 'admin123'))
print(response_data.text)