from infra.db.conexao import session
from models.livraria import Cliente
from infra.db.conexao import *
from flask import jsonify

class CrudCliente():
    
    @staticmethod
    def cadastrar_cliente(data:dict):
        try:
            novo_cliente = Cliente(
                nome=data['nome']
            )
            print(novo_cliente)
            session.add_all([novo_cliente])
            session.commit()
            session.close()
            return novo_cliente
        except Exception as e:
            print(e)
            session.rollback()
        
    @staticmethod
    def buscar_cliente(id):
        cliente = session.query(Cliente).filter(Cliente.id==id).first()
        return cliente
    
    @staticmethod
    def buscar_cliente_all():
        clientes = session.query(Cliente).all()
        return clientes
    
    @staticmethod
    def apagar_cliente(id):
        try:
            cliente = session.query(Cliente).filter(Cliente.id==id).one_or_none()
            session.delete(cliente)
            session.commit()
            session.close()
        except Exception as e:
            session.rollback()
        
    @staticmethod    
    def atualizar_cliente(id, cliente_data):
        cliente = session.query(Cliente).filter(Cliente.id==id).one_or_none()
        if cliente:
            cliente.nome = cliente_data["nome"]
            session.commit()
            session.close()
            return cliente
        return None
        