from flask import Flask,jsonify,request
from entity.cliente import ClienteEntity
from entity.livro import LivroEntity
from entity.compra import CompraEntity, ListaCompraFinal
from services.cliente_service import ClienteService
from services.livro_service import LivroService
from services.compra_service import CompraService

import json

app=Flask(__name__)

#-----------------------------------Busca all------------------------------------------
# @app.route('/clientes', methods=['GET'])
# def cliente():
#     clientes = ClienteService.get_all_clientes()
#     lista_clientes=[]
#     for cliente in clientes:
#         lista_clientes.append({
#             "id": cliente.id,
#             "nome": cliente.nome
#         })
#     return json.dumps(lista_clientes)

@app.route('/clientes', methods=['GET'])
def get_cliente():
    results = ClienteService.get_all_clientes()
    
    #Converter os resultados em objeto Pydantic
    clientes = [ClienteEntity(id=result.id, nome=result.nome) for result in results]
    
    #Serializar os resultados para JSON
    json_results = json.dumps([cliente.dict() for cliente in clientes])
    
    return json_results

# @app.route('/clientes', methods=['GET'])
# def cliente():
#     clientes = ClienteService.get_all_clientes()
#     json_result = json.dumps([{
#         'id': cliente.id,
#         'name':cliente.nome
#     } for cliente in clientes])
#     return json_result

#-------------------------------------Busca por id--------------------------------------
# @app.route('/clientes/<id>', methods=['GET'])
# def cliente_id(id):
#     cliente = ClienteService.get_cliente(id)
#     client_dict=cliente.__dict__
#     cliente = {"id":client_dict["id"], "nome":client_dict["nome"]}
#     return cliente

@app.route('/clientes/<id>', methods=['GET'])
def get_cliente_id(id):
    cliente = ClienteService.get_cliente(id)
    if cliente:
        #Criar uma instancia do modelo Pydantic
        objeto_model = ClienteEntity.from_orm(cliente)
        
        #Converta o modelo para dicionario
        objeto_dict = objeto_model.dict()
        
        #Serialize o dicionario no formato JSON
        json_data = json.dumps(objeto_dict)
        
        return json_data
    else:
        return jsonify({"Mensagem":"Esse cliente não existe"})


#---------------------------------------Create-----------------------------------------
@app.route('/clientes', methods=['POST'])
def create_clientes():
    #Obtenha os dados enviados da requisicao
    data = request.get_json()
    
    result = ClienteService.create_cliente(data)
    
    if result is None:
        return jsonify({"Mensagem":"Não foi possíve cadastrar o cliente"})
    else:
        return jsonify({"Mensagem":"Usuario cadastrado com sucesso"}), 201


#-----------------------------------Delete--------------------------------------------
@app.route('/clientes/<id>', methods=['DELETE'])
def delete_clientes(id):
    cliente = ClienteService.get_cliente(id)
    if cliente:
        ClienteService.delete_livro(id)
        return jsonify({"Message":"Cliente apagado com sucesso"})
    else:
        return jsonify({"Message":"Cliente não apagado"})
    
#-------------------------------------Atuaalizar----------------------------------------
@app.route("/clientes/<id>", methods=["PUT"])
def update_clientes(id):
    #Obtendo os dados do request
    data = request.get_json()
    
    result = ClienteService.update_cliente(id, data)
    
    if result is None:
        return jsonify({"Mensagem":"Não foi possíve atualizar o cliente"})
    else:
        return jsonify({"Mensagem":"Usuario atualizado com sucesso"}), 201


#=========================Livros=============================
@app.route('/livros', methods=['GET'])
def get_livro():
    results = LivroService.get_all_livros()
    
    if results is None:
        return jsonify({"Error":"Não foi encontrado nenhum livro"})
    
    #Converter os resultados em objeto Pydantic
    livros = [LivroEntity(id=result.id, nome=result.nome, autor=result.autor, editora=result.editora) for result in results]
    
    #Serializar os resultados para JSON
    json_results = json.dumps([livro.dict() for livro in livros])
    
    return json_results

@app.route('/livros/<id>', methods=['GET'])
def get_livro_id(id):
    livro = LivroService.get_livro(id)
    if livro:
        #Criar uma instancia do modelo Pydantic
        objeto_model = LivroEntity.from_orm(livro)
        
        #Converta o modelo para dicionario
        objeto_dict = objeto_model.dict()
        
        #Serialize o dicionario no formato JSON
        json_data = json.dumps(objeto_dict)
        
        return json_data
    else:
        return jsonify({"Mensagem":"Esse livro não existe"})


@app.route('/livros/', methods=['POST'])
def create_livros():
    #Obtenha os dados enviados da requisicao
    data = request.get_json()
    
    result = LivroService.create_livro(data)
    
    if result is None:
        return jsonify({"Mensagem":"Não foi possíve cadastrar esse livro"})
    else:
        return jsonify({"Mensagem":"Livro cadastrado com sucesso"}), 201


@app.route('/livros/<id>', methods=['DELETE'])
def delete_livros(id):
    livro = LivroService.get_livro(id)
    if livro:
        LivroService.delete_livro(id)
        return jsonify({"Message":"Livro apagado com sucesso"})
    else:
        return jsonify({"Message":"Livro não apagado"})
    

@app.route("/livros/<id>", methods=["PUT"])
def update_livros(id):
    #Obtendo os dados do request
    data = request.get_json()
    
    result = LivroService.update_livro(id, data)
    
    if result is None:
        return jsonify({"Mensagem":"Não foi possíve atualizar o livro"})
    else:
        return jsonify({"Mensagem":"Livro atualizado com sucesso"}), 201
    

#=========================Compra========================

@app.route('/compras', methods=['GET'])
def get_compra():
    compras = CompraService.get_all_compras()
    print(compras)
    try:
        if compras:
            #Criar uma instancia do modelo Pydantic
            objeto_model = ListaCompraFinal.from_orm(compras)
            # print(objeto_model)
            #Converta o modelo para dicionario
            objeto_dict = objeto_model.dict()
            
            #Serialize o dicionario no formato JSON
            json_data = json.dumps(objeto_dict)
           
        
            return json_data
        # else:
    except Exception as e:
        # return jsonify({"Mensagem":"Essa compra não existe"})
        return(e)
    

@app.route('/compras/<id>', methods=['GET'])
def get_compra_id(id):
    compra = CompraService.get_compra(id)
    if compra:
        #Criar uma instancia do modelo Pydantic
        objeto_model = CompraEntity.from_orm(compra)
        
        #Converta o modelo para dicionario
        objeto_dict = objeto_model.dict()
        
        #Serialize o dicionario no formato JSON
        json_data = json.dumps(objeto_dict)
        
        return json_data
    else:
        return jsonify({"Mensagem":"Essa compra não existe"})


@app.route('/compras', methods=['POST'])
def create_compras():
    
    #Obtenha os dados enviados da requisicao
    data = request.get_json()
    
    result = CompraService.create_compra(data)
    
    json_cadastrados = json.dumps(result)
    
    return json_cadastrados
    # if result is None:
    #     return jsonify({"Mensagem":"Não foi possíve cadastrar essa compra"})
    # else:
    #     return jsonify({"Mensagem":"Compra cadastrada com sucesso"}), 201
    
    


@app.route('/compras/<id>', methods=['DELETE'])
def delete_compras(id):
    compra = CompraService.get_compra(id)
    if compra:
        CompraService.delete_compra(id)
        return jsonify({"Message":"Compra apagada com sucesso"})
    else:
        return jsonify({"Message":"Compra não apagada"})
    

@app.route('/compras/<id>', methods=['PUT'])
def update_compras(id):
    #Obtendo os dados do request
    data = request.get_json()
    
    result = CompraService.update_compra(id, data)
   
    print(result)
    json_cadastrados = json.dumps(result)
    print(json_cadastrados)
    
    return json_cadastrados
    
    # if  is None:
    #     return jsonify({"Mensagem":"Não foi possíve atualizar o livro"})
    # else:
    #     return jsonify({"Mensagem":"Livro atualizado com sucesso"}), 201









if __name__=="__main__":
    app.run(debug=True)



