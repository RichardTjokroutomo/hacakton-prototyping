from flask import Flask, request, jsonify
import os

from test_connection import createEntry, deleteEntry, getEntry, getAllEntry


app = Flask(__name__)


# 1) insert row to db
# =============================================================================
# createEntry(location, origin, destination, status, name, customer_id, id_type, notes, flags)
@app.route('/insert-db', methods=['POST'])
def call_server():
    location = request.args.get('location')
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    status = request.args.get('status')
    name = request.args.get('name')
    customer_id = request.args.get('customer_id')
    id_type = request.args.get('id_type')
    notes = request.args.get('notes')
    flags = request.args.get('flags')

    usr_id = createEntry(location, origin, destination, status, name, customer_id, id_type, notes, flags)
    return jsonify({'usr_id': usr_id}), 200


# 2) delete row
# ===========================================================================
@app.route('/delete-db', methods=['POST'])
def call_server():
    rfid = request.args.get('rfid')
    deleteEntry(rfid)
    return jsonify({'msg': 'deletion success!'}), 200


# 3) get 1 row
# ===========================================================================
@app.route('/get-db', methods=['GET'])
def call_server():
    rfid = request.args.get('rfid')
    fetched_row = getEntry(rfid)
    json_dct = {'rfid': fetched_row[0], 'location': fetched_row[1], 'origin': fetched_row[2], 'destination': fetched_row[3], 'status':fetched_row[4], 'name':fetched_row[5], 'customer_id':fetched_row[6], 'id_type':fetched_row[7], 'notes':fetched_row[8], 'flags':fetched_row[9]}
    return jsonify(json_dct), 200



# 4) get all rows
# ===========================================================================
@app.route('/get-all-db', methods=['POST'])
def call_server():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return jsonify({'msg': 'hello!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
