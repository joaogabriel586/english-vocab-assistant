import sqlite3

DB = "vocab.db"

def conectar ():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela ():
    conn = conectar()
    conn.execute("""CREATE TABLE IF NOT EXISTS videos (
   id INTEGER PRIMARY KEY,
   youtube_id TEXT NOT NULL UNIQUE,
   url TEXT NOT NULL,
   titulo TEXT,
   adicionado_em TEXT NOT NULL ) """)
    conn.commit()
    conn.close()

criar_tabela()