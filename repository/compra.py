from infra.db.conexao import  session
from models.livraria import Livro
from models.livraria import Cliente
from models.livraria import Compra
from entity.livro import LivroEntity
from entity.compra import CompraEntity,ListaCompraFinal
import json
import pprint

class CrudCompra():

 
    
    # @staticmethod
    # def cadastrar_compra(compra_data: dict):
    #     try:
    #         cliente = session.query(Cliente).filter_by(nome=compra_data['cliente']).one_or_none()
            
    #         livros=compra_data['livros']
            
    #         compra = Compra()
    #         compra.cliente=cliente.id
            
    #         for livro in livros:
    #             livro = Livro(nome=livro['livro'], autor=livro['autor'], editora=livro['editora'])
    #             compra.livro_objeto.append(livro)
                

    #         session.add_all([compra])
    
    #         session.commit()
    #         session.close()
            
    #         compra_json = json.dumps(compra.as_dict())
    #         print(compra_json)
            
    #     except Exception as e:
    #         session.rollback()
            
    
    # @staticmethod
    # def cadastrar_compra(compra_data: dict):
    #     try:
    #         cliente = session.query(Cliente).filter_by(nome=compra_data['cliente']).one_or_none()

    #         livros = compra_data['livros']
            
    #         compra = Compra(
    #             cliente=cliente.id,
    #         )
    #         for livro in livros:
    #         # Nessa parte vc tem que criar o objeto da table de livros e passar os atributos
    #             livro_obj = Livro(
    #                 nome = livro['nome'],
    #                 autor = livro['autor'],
    #                 editora = livro['editora'],
    #             )
    #         # aqui vc adiciona os objetos da tablea livro
    #         compra.livro_objeto.append(livro_obj)
        
    #     # faz o commit da compra, no atributo livro_objeto estão os livros que seram commitados tbm
    #         session.add(compra)
    #         session.commit()
    #         session.close()
    #         compra_json = json.dumps(compra.as_dict())
    #         print(compra_json)
    #     except Exception as e:
    #         session.rollback()
            
    @staticmethod
    def cadastrar_compra(compra_data: dict):
        try:
            cliente = session.query(Cliente).filter(Cliente.nome == compra_data['cliente']).first()
            livros = compra_data['livros']
            
            compra = Compra(
                id_cliente = cliente.id,
            )

            for livro in livros:
            # Nessa parte vc tem que criar o objeto da table de livros e passar os atributos
                print(livro)
                livro_obj = Livro(
                    nome = livro['livro'],
                    autor = livro['autor'],
                    editora = livro['editora'],
                )
                # aqui vc adiciona os objetos da tablea livro
                compra.livro_objeto.append(livro_obj)
        
        # faz o commit da compra, no atributo livro_objeto estão os livros que seram commitados tbm
            session.add(compra)
            session.flush()
            session.commit()
           
           
            dados_cadastrados={
               "id_compra": compra.id,
               "id_cliente": compra.id_cliente,
               "livros" : [{
                   "nome":livro.nome,
                   "autor":livro.autor,
                   "editora":livro.editora
               }for livro in compra.livro_objeto]
           }
            session.close()
            
            return dados_cadastrados
        
        except Exception as e:
            print(e)
            session.rollback()            
            
    @staticmethod
    def buscar_compra(id):
        try:
            compra = session.query(Compra).filter(Compra.id == id).first()
        
            if compra:
                cliente = session.query(Cliente).filter(Cliente.id == compra.id_cliente).first()
            
                livros = []
                for livro in compra.livro_objeto:
                    livro_data = LivroEntity(
                        nome = livro.nome,
                        autor = livro.autor,
                        editora=livro.editora
                    )
                    livros.append(livro_data)
                    
                dados_compra = CompraEntity(
                    id = compra.id,
                    id_cliente = compra.id_cliente,
                    nome= cliente.nome,
                    livros=livros
                )
                return dados_compra
            else:
                return None
        except Exception as e:
            print(e)
            session.rollback()
    
                
    # @staticmethod
    # def buscar_compra_all():
#         try:
#         # Consultar todas as compras usando a sessão
#             todas_compras = session.query(Compra).all()
#             return todas_compras
#         except Exception as e:
#             print(f"Erro ao obter todas as compras: {e}")
#             return []

# # Chamando a função para obter todas as compras
#     compras = buscar_compra_all()

# # Exemplo de impressão das informações de cada compra
#     for compra in compras:
#         print(f'ID da Compra: {compra.id}')
#         print(f'ID do Cliente: {compra.id_cliente}')
#         print('Livros comprados:')
#         for livro in compra.livro_objeto:
#             print(f' - Livro ID: {livro.id}, Nome: {livro.nome}, Autor: {livro.autor}, Editora: {livro.editora}')
#         print('-' * 30)
        
        
    def buscar_compra_all():
        try:
            resultados=[]
            compras = session.query(Compra).all()
            
            if compras is not None:
                for compra in compras:
                
                    livros = []
                    for livro in compra.livro_objeto:
                        livro_data = LivroEntity(
                        nome = livro.nome,
                        autor = livro.autor,
                        editora=livro.editora
                        )
                        livros.append(livro_data)
                  
                    cliente = session.query(Cliente).filter(Cliente.id==compra.id_cliente).first()
                
                    dados_compra = CompraEntity(
                        id = compra.id,
                        id_cliente = compra.id_cliente,
                        nome= cliente.nome,
                        livros=livros                          
                    )
                    
                    resultados.append(dados_compra)
                    
                resultados = ListaCompraFinal(compras = resultados)

                return resultados
            else:
                return None
        except Exception as e:
                print(e)
                session.rollback()
        
 
    @staticmethod
    def delete_compra(id):
        try:
            compra = session.query(Compra).filter(Compra.id == id).one_or_none()
            session.delete(compra)
            session.commit()
        except Exception as e:
            session.rollback()
            
            
    @staticmethod    
    def atualizar_compra(id, compra_data):
        try:
            compra = session.query(Compra).filter(Compra.id == id).one_or_none()
            print(compra)
            cliente = session.query(Cliente).filter(Cliente.nome == compra_data['nome']).first()
            
            if  compra is not None:
                compra = Compra(
                    id_cliente = cliente.id
                )
            
                livros = compra_data['livros']

                for livro in livros:
                # Nessa parte vc tem que criar o objeto da table de livros e passar os atributos
                    livro_obj = Livro(
                        nome = livro['livro'],
                        autor = livro['autor'],
                        editora = livro['editora'],
                    )
                    # aqui vc adiciona os objetos da tablea livro
                    compra.livro_objeto.append(livro_obj)
                    
        
                # faz o commit da compra, no atributo livro_objeto estão os livros que seram commitados tbm
                
                dados_compra = CompraEntity(
                    id = compra.id,
                    id_cliente = compra.id_cliente,
                    nome=cliente.nome,
                    livros=livros
                )
                session.add([dados_compra])
                session.flush()
                session.commit()
                
                session.close()
                
                # dados_cadastrados={
                #     "id_compra": id,
                #     "id_cliente": compra.id_cliente,
                #     # "nome": cliente.nome,
                #     "livros" : [{
                #         "nome":livro.nome,
                #         "autor":livro.autor,
                #         "editora":livro.editora
                #     }for livro in compra.livro_objeto]
                # }
                
                print(dados_compra)
                
                return dados_compra
            else:
                return None
        except Exception as e:
            print(e)
            session.rollback()      
            