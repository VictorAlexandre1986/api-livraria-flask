from infra.db.conexao import session
from models.livraria import Livro


class CrudLivro():

    @staticmethod
    def cadastrar_livro(data: dict):
        try:
            novo_livro = Livro(
                nome=data['nome'],
                autor=data['autor'],
                editora=data['editora']
            )
            session.add_all([novo_livro])
            session.commit()
            session.close()
            return novo_livro
        except Exception as e:
            print(e)
            session.rollback()

    @staticmethod
    def buscar_livro(id):
        livro = session.query(Livro).filter(Livro.id == id).one_or_none()
        return livro
    
    @staticmethod
    def buscar_livro_all():
        livros = session.query(Livro).all()
        return livros

    @staticmethod
    def apagar_livro(id):
        try:
            livro = session.query(Livro).filter(Livro.id == id).one_or_none()
            session.delete(livro)
            session.commit()
        except Exception as e:
            session.rollback()
    
 
    @staticmethod
    def atualizar_livro(id_livro, livro_data):
        livro = session.query(Livro).filter(Livro.id==id_livro).one_or_none()
        if livro:
            print(livro)
            livro.nome = livro_data['nome']
            livro.autor = livro_data['autor']
            livro.editora = livro_data['editora']
            session.commit()
            session.close()
            return livro
        return None