from pydantic import BaseModel

class ClienteEntity(BaseModel):
    id : int | None
    nome : str | None
    
    class Config:
        orm_mode = True