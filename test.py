import requests
import json
jsonEncoder = json.JSONEncoder()
test_data = {
    "api-key": "Key123",
    "message": [{'role': 'user', 'content': 'Hello!'}],
    "max_tokens": 100,
    "temperature": 0.7,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": None
}
response = requests.get('http://127.0.0.1:5000/chat/CuteGPT', json=test_data)
print(response.text)