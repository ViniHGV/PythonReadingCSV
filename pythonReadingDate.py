import sqlite3

connector = sqlite3.connect("Loja.db")
cursor = connector.cursor()

CodRrepres = []
TipoPess = []
NomeFan = []
ComissaoBase = []

i = 0
arq = open("Repres.CSV", "r")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
        CodRrepres.append(int(s[0]))
        TipoPess.append(str(s[1]))
        NomeFan.append(str(s[2]))
        ComissaoBase.append(float(str(s[3].replace(",", "."))))
    s = arq.readline().rstrip()
    i += 1
arq.close

sql = """
    CREATE TABLE IF NOT EXISTS Repres
    (
    CODREPRES integer primary key,
    TIPOPESS string,
    NOMEFAN stirng,
    COMISSAOBASE numeric
    )
"""
cursor.execute(sql)

print("Tabela Repres Criada 🚀")

for i in range(len(CodRrepres)):
    sql = f"""
        INSERT INTO Repres (CODREPRES, TIPOPESS, NOMEFAN, COMISSAOBASE)
        VALUES ({CodRrepres[i]}, '{TipoPess[i]}', '{NomeFan[i]}', {ComissaoBase[i]})
    """
    cursor.execute(sql)

print("Valores Adicionados com Sucesso!")


connector.commit()
cursor.close
connector.close()
