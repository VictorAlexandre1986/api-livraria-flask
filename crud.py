from repository.cliente import CrudCliente
from repository.livro import CrudLivro




if __name__=="__main__":
    # cliente = CrudCliente()
    # cliente.cadastrar_cliente("")
    
    livro = CrudLivro()
    livro.cadastrar_livro("O iluminado","Stephen King","FSC")
    
