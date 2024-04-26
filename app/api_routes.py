from flask import jsonify, request, url_for
from app import app, db
from app.models import Product
from flask import render_template

#Essa rota é a rota de criação do produto
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        type=data['type'],
        corante=data['corante'],
        transgênico=data['transgenico'],
        aditivos_quimicos=data['aditivos'],
        organismo_geneticamente_modificado=data['ogm']
    )
    db.session.add(new_product)
    db.session.commit()

    # URL da página de produtos cadastrados:
    products_url = url_for('get_products', _external=True)

    # Retorne a resposta JSON com a mensagem e a URL da página de produtos cadastrados
    return jsonify({
        'message': 'Produto cadastrado com sucesso',
        'products_url': products_url
    }), 201

# Apresentação do produtos em HTML:
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return render_template('getproducts.html', products=products)

 # Separar a rota da resposta em JSON e da resposta em HTML
# Rota para obter todos os produtos em formato JSON:
@app.route('/api/products/json', methods=['GET'])
def get_products_json():
    products = Product.query.all()
    products_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'type': product.type,
            'corante': product.corante,
            'transgenico': product.transgênico,
            'aditivos_quimicos': product.aditivos_quimicos,
            'organismo_geneticamente_modificado': product.organismo_geneticamente_modificado
        }
        products_list.append(product_data)
    return jsonify(products_list)

