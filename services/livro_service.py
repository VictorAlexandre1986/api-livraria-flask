from repository.livro import CrudLivro


class LivroService:

    @staticmethod
    def get_all_livros():
        return CrudLivro.buscar_livro_all()

    @staticmethod
    def get_livro(id_livro):
        return CrudLivro.buscar_livro(id_livro)

    @staticmethod
    def create_livro(livro_data):
        return CrudLivro.cadastrar_livro(livro_data)
    
    @staticmethod
    def update_livro(livro_id, livro_data):
        return CrudLivro.atualizar_livro(livro_id, livro_data)
    
    @staticmethod
    def delete_livro(livro_id):
        return CrudLivro.apagar_livro(livro_id)