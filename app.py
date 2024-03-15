from flask import Flask, request
import http.client

def send_post_request(url, headers, data):
    conn = http.client.HTTPSConnection(url.split('/')[2])
    conn.request("POST", url, data, headers)
    response = conn.getresponse()
    return response.read().decode('utf-8')

app = Flask(__name__)

@app.route('/chat/<Model>', methods=['GET'])
def forward(Model):
    # Get the POST request JSON data
    data = request.get_json()

    new_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + data['api-key']
    }
    new_data = {
        'model': Model,
        'message': data['message'],
        'max_tokens': data['max_tokens'],
        'temperature': data['temperature'],
        'top_p': data['top_p'],
        'frequency_penalty': data['frequency_penalty'],
        'presence_penalty': data['presence_penalty'],
        'stop': data['stop']
    }

    return send_post_request('https://api.openai.com/v1/chat/completions', new_headers, new_data)

if __name__ == '__main__':
    app.run()