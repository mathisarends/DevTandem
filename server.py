from flask import Flask, request, jsonify

app = Flask(__name__)

# Zombie-Server Schnittstellen

# POST /z/init
@app.route('/z/init', methods=['POST'])
def zombie_init(): 
    #data = request.get_json()

    # Hier können die empfangenen Daten verarbeitet werden...
    return jsonify({ "message": "Zombie Initialisierung erfolgreich!" }), 200 #Status 200 = OK


# GET /z/update
@app.route('/z/update', methods=['GET'])
def zombie_update():
    #data = request.get_json()

    # Hier können die empfangenen Daten verarbeitet werden...
    return jsonify({"speed": 0.5, "direction": 0.7, "rotation": 0.2}), 200 #Status 200 = OK


# Human Schnittstellen

# POST /h/init
@app.route('/h/init', methods=['POST'])
def human_init():
    data = request.get_json()

    # Hier können die empfangenen Daten verarbeitet werden...
    return jsonify({"message": "Human Initialization Successful"}), 200 #Status 200 = OK


# GET /h/update
@app.route('/h/update', methods=['GET'])
def human_update():
    #data = request.get_json()
    # Hier können die empfangenen Daten verarbeitet werden...

    return jsonify({"speed": 0.8, "direction": 0.1}), 200 #Status 200 = OK


# GET-Route MAIN
@app.route('/', methods=['GET'])
def get_route():
    return 'GET Route: Hello, World!'


if __name__ == '__main__':
    # Starte den Webserver auf Port 5000 (Standardport für Flask)
    app.run(debug=True)