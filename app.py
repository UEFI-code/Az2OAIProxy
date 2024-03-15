from flask import Flask, request
import http.client
import json

jsonEncoder = json.JSONEncoder()

def send_post_request(url, headers, data):
    conn = http.client.HTTPSConnection(url.split('/')[2])
    conn.request("POST", url, data, headers)
    response = conn.getresponse()
    return response.read().decode('utf-8'), response.status

app = Flask(__name__)

@app.route('/chat/<model_name>', methods=['POST'])
def forward(model_name):
    # Get the POST request JSON headers and data
    headers = request.headers
    data = request.get_json()

    new_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + headers['api-key']
    }
    new_data = {
        'model': model_name,
        'messages': data['message'],
        'max_tokens': data['max_tokens'],
        'temperature': data['temperature'],
        'top_p': data['top_p'],
        'frequency_penalty': data['frequency_penalty'],
        'presence_penalty': data['presence_penalty'],
        'stop': data['stop']
    }

    #print(f'Headers: {new_headers}, Data: {new_data}')

    return send_post_request('https://api.openai.com/v1/chat/completions', new_headers, jsonEncoder.encode(new_data))

if __name__ == '__main__':
    app.run()