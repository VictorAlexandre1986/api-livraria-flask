from repository.cliente import CrudCliente


class ClienteService:

    @staticmethod   
    def get_all_clientes():
        return CrudCliente.buscar_cliente_all()

    @staticmethod
    def get_cliente( id_cliente):
        return CrudCliente.buscar_cliente(id_cliente)

    @staticmethod
    def create_cliente(cliente_data):
        return CrudCliente.cadastrar_cliente(cliente_data)
    
    @staticmethod
    def update_cliente(cliente_id, cliente_data):
        return CrudCliente.atualizar_cliente(cliente_id, cliente_data)
    
    @staticmethod
    def delete_livro(cliente_id):
        return CrudCliente.apagar_cliente(cliente_id)