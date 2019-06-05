from flask import Flask, request, jsonify
from database import *

app = Flask(__name__)

@app.route('/start_stream', methods=['POST'])
def start_stream():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json    #['user_name']
        user_name = data['user_name']
        password = data['sifra']
        predmet = data['predmet']
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        try:
            profesor_id = prof_id(user_name, password)
        except ValueError as e:
            return jsonify({'status': str(e)})

        try:
            predmet_id = pred_id(predmet)
        except ValueError as e:
            return jsonify({'status': str(e)})

        try:
            provera_prof_pred(profesor_id, predmet_id)
        except ValueError as e:
            return jsonify({'status': str(e)})

        stream_id = unesi_stream(ip)
        unesi_predavanje(predmet_id, stream_id)




        return jsonify({'status': 'ok'})

@app.route('/reserve_pc', methods=['POST'])
def reserve_pc():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json    #['user_name']
        indeks = data['indeks']
        password = data['sifra']
        kod = data['kod']

        try:
            student_id = stud_id(indeks, password)
        except ValueError as e:
            return jsonify({'status': str(e)})

        try:
            racunar_id = rac_id(kod)
        except ValueError as e:
            return jsonify({'status': str(e)})

        try:
            rac_zauzet(racunar_id)
        except ValueError as e:
            return jsonify({'status': str(e)})

        unesi_koristi(student_id, racunar_id)


        return jsonify({'status': 'ok'})

@app.route('/get_ip', methods=['POST'])
def get_ip():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json    #['user_name']
        kod = data['kod']

        try:
            racunar_id = rac_id(kod)
        except ValueError as e:
            return jsonify({'status': str(e)})

        try:
            student_id = rac_stud_id(racunar_id)
        except ValueError as e:
            return jsonify({'status': str(e)})

        try:
            stream_id, stream_ip = stud_stream_ip(student_id)
        except ValueError as e:
            return jsonify({'status': str(e)})

        unesi_prisustvo(student_id, stream_id)

        ip = stream_ip
        return jsonify({'status': 'ok', 'ip': ip})

@app.route('/is_running', methods=['POST'])
def is_running():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if stream_pokrenut(ip):
        return jsonify({})
    else:
        return jsonify({'status': 'moze'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
