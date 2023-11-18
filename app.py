from flask import Flask, render_template, request

app = Flask(__name__)

# GET-Route
@app.route('/', methods=['GET'])
def get_route():
    #return 'GET Route: Hello, World!'
    name = "Mathis"
    age = 21
    return render_template('index.html', 
                           name=name,
                           age=age,
                           ) #Nutzung von Template im HTML-Template

# POST-Route
@app.route('/', methods=['POST'])
def post_route():
    data = request.get_data(as_text=True)
    return f'POST Route: Received data - {data}'

if __name__ == '__main__':
    # Starte den Webserver auf Port 5000 (Standardport für Flask)
    app.run(debug=True)