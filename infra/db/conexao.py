import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conexao = 'sqlite:///'+os.path.join(BASE_DIR, 'livraria.db')

engine = create_engine(conexao, echo=True)

Base = declarative_base()


session = sessionmaker()(bind=engine)


association_table = Table(
    'compra_livro',
    Base.metadata,
    Column('compra_id', Integer(), ForeignKey('compra.id')),
    Column('livro_id', Integer(), ForeignKey('livro.id')),
    extend_existing=True
 )


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer(), primary_key=True)
    nome = Column(String(250), nullable=False)
    compra = relationship('Compra', backref="cliente", cascade='all, delete')
    
    
    def __repr__(self):
        return f'<Cliente : {self.nome}>'

    def as_dict(self):
        return {c.id: getattr(self, c.id) for c in self.__table__columns}


class Livro(Base):
    __tablename__ = 'livro'

    id = Column(Integer(), primary_key=True)
    nome = Column(String(255))
    autor = Column(String(255))
    editora = Column(String(255))
    compras_objeto = relationship('Compra', secondary=association_table, back_populates='livro_objeto')
    
    
    def __repr__(self):
        return f'<Livro : {self.id}, autor:{self.autor}, editora:{self.editora}> '

    def as_dict(self):
        return {c.id: getattr(self, c.id) for c in self.__table__columns}


class Compra(Base):
    __tablename__ = 'compra'

    id = Column(Integer(), primary_key=True)
    id_cliente = Column(Integer(), ForeignKey("cliente.id"))
    livro_objeto = relationship('Livro', secondary=association_table, back_populates='compras_objeto')
 
 
    
    def __repr__(self):
        return f'<Compra : {self.id} {self.id_cliente} {self.id_livro}>'

    def as_dict(self):
        return {c.id: getattr(self, c.id) for c in self.__table__columns}



