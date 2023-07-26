from pydantic import BaseModel
from typing import List
from entity.livro import LivroEntity

class CompraEntity(BaseModel):
    id: int 
    id_cliente: int
    nome: str | None
    livros : List[LivroEntity] 
    

    class Config:
        orm_mode = True
        
        
class ListaCompraFinal(BaseModel):
    compras: List[CompraEntity] 
    
    class Config:
        orm_mode = True
    
# class CompraEntity(BaseModel):
#     id: int
#     cliente: ClienteEntity
#     livros : List[LivroEntity]
#     quantidade: int

#     class Config:
#         orm_mode = True
    