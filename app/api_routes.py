from flask import jsonify, request, url_for
from app import app, db
from app.models import Product
from flask import render_template

#Essa rota é a rota de criação de um produto:
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        type=data['type'],
        corante=data['corante'],
        transgenico=data['transgenico'],
        aditivos_quimicos_sinteticos=data['aditivos_quimicos_sinteticos'], #  erro aqui keyError
        organismos_geneticamente_modificados=data['organismos_geneticamente_modificados']
    )
    db.session.add(new_product)
    db.session.commit()

    # URL da página de produtos cadastrados:
    products_url = url_for('products', _external=True)

    # Retorne a resposta JSON com a mensagem e a URL da página de produtos cadastrados
    return jsonify({
        'message': 'Produto cadastrado com sucesso',
        'products_url': products_url
    }), 201

# Busca e renderiza os produtos em HTML:
@app.route('/api/products', methods=['GET'])
def render_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

 # Separamos a rota da resposta em JSON e da resposta em HTML
# Rota para obter todos os produtos em formato JSON:
@app.route('/api/products/json', methods=['GET'])
def products_json():
    products = Product.query.all()
    products_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'type': product.type,
            'corante': product.corante,
            'transgenico': product.transgenico,
            'aditivos_quimicos_sinteticos': product.aditivos_quimicos_sinteticos,
            'organismos_geneticamente_modificados': product.organismos_geneticamente_modificados
        }
        products_list.append(product_data)
    return jsonify(products_list)
