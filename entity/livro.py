from pydantic import BaseModel

class LivroEntity(BaseModel):
    id: int | None
    nome: str
    autor: str
    editora : str 
    
    class Config:
        orm_mode = True
    