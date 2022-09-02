'''
Ligação com o banco de dados

'''

from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from cadastro import models 
from cadastro.config import settings


engine = create_engine(settings.database.url, echo=False)

# Cria o banco de dados
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)


# Para crir o banco python databas.py
