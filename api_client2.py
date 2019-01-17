import requests, json



## private String url = "http://110.13.71.93:9292/api/V1/mail"; // raspberry
## private String url = "http://211.239.124.246:19808/api/V1/mail"; // fun25

data = [{ 'subject':'test', 'message':'xxxxx'},{ 'subject':'test', 'message':'xxxx1'}]
response = requests.post('http://211.239.124.246:19808/api/V1/mail', json.dumps(data))



print("CODE====="+response.text)
## assert response.status_code == 200

print(response.text)

for repo in response.json():
    print ('[{}] {}'.format(repo['language'], repo['name']))