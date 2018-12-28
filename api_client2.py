import requests, json

data = [{ 'subject':'test', 'message':'xxxxx'},{ 'subject':'test', 'message':'xxxx1'}]
response = requests.post('http://localhost:9292/api/V1/mail', json.dumps(data))



print("CODE====="+response.text)
assert response.status_code == 200

print(response.text)

for repo in response.json():
    print ('[{}] {}'.format(repo['language'], repo['name']))