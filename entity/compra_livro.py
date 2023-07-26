from pydantic import BaseModel


class CompraLivrosEntity(BaseModel):
    id_compra: int
    id_livro: int
    quantidade: int

    class Config:
        orm_mode = True