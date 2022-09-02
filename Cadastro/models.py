'''
Pelo que eu entendi aqui é onde é modelado a classe 

'''

from datetime import datetime
from sqlmodel import Field, SQLModel
from typing import Optional
from pydantic import validator


class Livro(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    titulo: str
    autor: str
    editora: str
    edicao: str
    ano_publicacao: int
    local_armazenado: str
    ano_compra: int
    data_cadastro: datetime = Field(default_factory=datetime.now)

    @validator("ano_publicacao", "ano_compra")
    def validar_ano(cls, valor, field):
        if valor < 1900 or valor > 2100:
            raise RuntimeError(f"{field.name} precisa ter um ano valido")
        return valor


'''
# Para executar no terminal python models.py

try:
    livro = Livro(titulo="Python", autor="Manoel", editora="Saraiva", edicao="Primeira",
                  ano_publicacao=2220, local_armazenado="casa", ano_compra=1901)
except RuntimeError:
    print('Como tratar o erro')

'''
