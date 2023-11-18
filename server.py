from flask import Flask, request

app = Flask(__name__)

# GET-Route
@app.route('/', methods=['GET'])
def get_route():
    return 'GET Route: Hello, World!'

# POST-Route
@app.route('/', methods=['POST'])
def post_route():
    data = request.get_data(as_text=True)
    return f'POST Route: Received data - {data}'

if __name__ == '__main__':
    # Starte den Webserver auf Port 5000 (Standardport für Flask)
    app.run(debug=True)