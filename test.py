import requests
import json
jsonEncoder = json.JSONEncoder()

test_headers = {
    'Content-Type': 'application/json',
    "api-key": "Key123",
}
test_data = {
    "message": [{'role': 'user', 'content': 'Hello!'}],
    "max_tokens": 100,
    "temperature": 0.7,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": None
}
response = requests.post('http://127.0.0.1:5000/chat/CuteGPT', headers=test_headers, data=jsonEncoder.encode(test_data))
print(response.text)