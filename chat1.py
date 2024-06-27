from flask import Flask, jsonify, request

app = Flask(__name__)

# Inicjalizacja expandera
expander = XL9535(bus_number=1, device_address=0x20)

@app.route('/set_pin', methods=['POST'])
def set_pin():
    try:
        data = request.json
        pin = data['pin']
        value = data['value']
        expander.set_pin(pin, value)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/get_pin/<int:pin>', methods=['GET'])
def get_pin(pin):
    try:
        value = expander.read_register(0x01) & (1 << pin)
        return jsonify({'status': 'success', 'value': bool(value)})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
