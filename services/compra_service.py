from repository.compra import CrudCompra
from repository.cliente import CrudCliente
from repository.livro import CrudLivro
from models.livraria import Compra

class CompraService:
        
    @staticmethod
    def get_all_compras():
        return CrudCompra.buscar_compra_all()

    @staticmethod
    def get_compra(id_compra):
        return CrudCompra.buscar_compra(id_compra)

    @staticmethod
    def create_compra(compra_data):
        return CrudCompra.cadastrar_compra(compra_data)
    
    @staticmethod
    def update_compra(id,compra_data):
        return CrudCompra.atualizar_compra(id, compra_data)
    
    @staticmethod
    def delete_compra(compra_id):
        return CrudCompra.delete_compra(compra_id)