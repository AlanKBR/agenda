import sqlite3

conn = sqlite3.connect("instance/calendario.db")
c = conn.cursor()
try:
    c.execute(
        "ALTER TABLE calendar_event ADD COLUMN "
        "all_day BOOLEAN NOT NULL DEFAULT 0;"
    )
    print("Coluna all_day adicionada com sucesso.")
except Exception as e:
    print("Erro ou coluna já existe:", e)
conn.commit()
conn.close()
