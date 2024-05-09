from app import app
from flask import jsonify



# Manipulador de erro para KeyErrors
@app.errorhandler(KeyError)
def handle_key_error(e):
    return jsonify({'error': 'Chave ausente no JSON enviado'}), 400

if __name__ == '__main__':
    app.run(debug=True)