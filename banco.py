import sqlite3

DB = "vocab.db"

def conectar ():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela_videos ():
    conn = conectar()
    conn.execute(""" CREATE TABLE IF NOT EXISTS videos (
   id INTEGER PRIMARY KEY,
   youtube_id TEXT NOT NULL UNIQUE,
   url TEXT NOT NULL,
   titulo TEXT,
   adicionado_em TEXT NOT NULL ) """)
    conn.commit()
    conn.close()

def criar_tabela_palavras ():
    conn = conectar()
    conn.execute(""" CREATE TABLE IF NOT EXISTS palavras (
    id INTEGER PRIMARY KEY,
    palavra TEXT NOT NULL UNIQUE,
    conhecida INTEGER NOT NULL ) """)
    conn.commit()
    conn.close()

def criar_tabela_aparicoes ():
    conn = conectar()
    conn.execute(""" CREATE TABLE IF NOT EXISTS aparicoes (
    video_id INTEGER NOT NULL,
    palavra_id INTEGER NOT NULL,
    vezes INTEGER NOT NULL,
    PRIMARY KEY (video_id, palavra_id),
    FOREIGN KEY (video_id) REFERENCES videos (id),
    FOREIGN KEY (palavra_id) REFERENCES palavras (id)) """)
    conn.commit()
    conn.close()

criar_tabela_videos()
criar_tabela_palavras()
criar_tabela_aparicoes()

conn = conectar()
resultado = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
for linha in resultado:
    print(linha["name"])
conn.close()