from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/start_stream', methods=['POST'])
def start_stream():
    if request.headers['Content-Type'] == 'application/json':
        nesto = request.json    #['user_name']
        print(nesto)
        return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
