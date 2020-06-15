import requests

#url = 'http://60.205.178.32:3002/file-upload'
url = 'http://47.94.108.78/file-upload'
result_str = 'hello world, hello china, hello Beijing'
file = 'filename.csv'
file_type = 'bus'
data = {'name': file, 'type': file_type, 'result': result_str}
response = requests.post(url,data=data)
print(response.text)
#http://60.205.178.32:3002/file-upload