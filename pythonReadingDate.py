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

i = 0

CODCLIFOR = []
TIPOCF = []
CODREPRES = []
NOMEFAN = []
CIDADE = []
UF = []
CODMUNICIPIO = []
TIPOPESSOA = []
COBRBANC = []
PRAZOPGTO = []

arq = open("FornClien.CSV")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
        CODCLIFOR.append(float(s[0]))
        TIPOCF.append(int(s[1]))
        CODREPRES.append(str(s[2]))
        NOMEFAN.append(str(s[3]))
        CIDADE.append(str(s[4]))
        UF.append(str(s[5]))
        CODMUNICIPIO.append(str(s[6]))
        TIPOPESSOA.append(int(s[7]))
        COBRBANC.append(int(s[8]))
        PRAZOPGTO.append(str(s[9]))
    s = arq.readline().rstrip()
    i += 1
arq.close

sql = """
    CREATE TABLE IF NOT EXISTS FornClien
    (
    CODCLIFOR numeric primary key,
    TIPOCF integer,
    CODREPRES string,
    NOMEFAN string,
    CIDADE string,
    UF string,
    CODMUNICIPIO string,
    TIPOPESSOA integer,
    COBRBANC integer,
    PRAZOPGTO string
    )
"""
cursor.execute(sql)

for i in range(len(CODCLIFOR)):
    sql = f"""
        INSERT INTO FornClien (CODCLIFOR, TIPOCF, CODREPRES, NOMEFAN, CIDADE, UF, CODMUNICIPIO, TIPOPESSOA, COBRBANC, PRAZOPGTO)
        VALUES ({CODCLIFOR[i]}, {TIPOCF[i]}, '{CODREPRES[i]}', '{NOMEFAN[i]}', '{CIDADE[i]}', '{UF[i]}', '{CODMUNICIPIO[i]}', {TIPOPESSOA[i]}, {COBRBANC[i]}, '{PRAZOPGTO[i]}')
    """
    cursor.execute(sql)

print("Valores Adicionados com Sucesso!")

connector.commit()
cursor.close
connector.close()
