"""
Classe para conexão ao banco de dados SqlLite3
"""

import sqlite3 as lite


class LivrosBD:
    def __init__(self, arquivo: object) -> object:
        self.conn = lite.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(
        self,
        titulo: object,
        autor: object,
        editora: object,
        edicao: object,
        ano: object,
        local: object,
        data_compra: object,
    ) -> object:
        consulta = 'INSERT OR IGNORE INTO livros (titulo, autor, editora, edicao, ano, local, data_compra) VALUES (?, ?, ?, ?, ?, ?, ? )'
        self.cursor.execute(
            consulta, (titulo, autor, editora, edicao, ano, local, data_compra)
        )
        self.conn.commit()

    def editar(
        self, titulo, autor, editora, edicao, ano, local, data_compra, id
    ):
        consulta = 'UPDATE OR IGNORE livros SET titulo=?, autor=?, editora=?, edicao=?, ano=?, local=?, data_compra=? WHERE id=?'
        self.cursor.execute(
            consulta,
            (titulo, autor, editora, edicao, ano, local, data_compra, id),
        )
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM livros WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM livros')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM livros WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar_bd(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    livro = LivrosBD('/LivrosBD.db3')

    # livro.inserir('Programação em Python 3', 'Mark Summerfield', 'Alta Books', 'primeira', '2013', 'Casa', '')
    livro.listar()
