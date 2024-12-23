# API - É um lugar para disponibilizar recursos e/ou funcionalidades.
# 1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.\
# 2. URL base - localhost
# 3. Endpoins 
    # - localhost/livros (GET)
    # - localhost/livros/id (POST)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)

# 4. Quais recursos - livros

# Utilizando o flask.


from flask import Flask, jsonify, request


app = Flask(__name__)

livros = [
    {
        "id": "1",
        "titulo": "Teste 1",
        "autor": "Autor desconhecido 1"
    },
    {
        "id": "2",
        "titulo": "Teste 2",
        "autor": "Autor desconhecido 2"
    },
    {
        "id": "3",
        "titulo": "Teste 3",
        "autor": "Autor desconhecido 3"
    }
]


# Consultar todos
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar id
@app.route('/livros/<id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


#editar
@app.route('/livros/<id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for index, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[index].update(livro_alterado)
            return jsonify(livros[index])


#Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


#excluir
@app.route('/livros/<id>', methods=['DELETE'])
def excluir_livros(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
    return jsonify(livros)

#iniciando app
app.run(port=5000, host='localhost', debug=True)