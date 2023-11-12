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
    NOMEFAN string,
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

CodCliFor = []
TipoCF = []
CodRepres = []
NomeFan = []
Cidade = []
Uf = []
CodMunicipio = []
TipoPessoa = []
Cobranc = []
PrazoPgto = []

arq = open("FornClien.CSV")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
        CodCliFor.append(int(str(s[0].replace(".", ""))))
        TipoCF.append(int(s[1]))
        CodRepres.append(str(s[2]))
        NomeFan.append(str(s[3]))
        Cidade.append(str(s[4]))
        Uf.append(str(s[5]))
        CodMunicipio.append(str(s[6]))
        TipoPessoa.append(int(s[7]))
        Cobranc.append(int(s[8]))
        PrazoPgto.append(str(s[9]))
    s = arq.readline().rstrip()
    i += 1
arq.close

sql = """
    CREATE TABLE IF NOT EXISTS FornClien
    (
    CODCLIFOR integer primary key,
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

for i in range(len(CodCliFor)):
    sql = f"""
        INSERT INTO FornClien (CODCLIFOR, TIPOCF, CODREPRES, NOMEFAN, CIDADE, UF, CODMUNICIPIO, TIPOPESSOA, COBRBANC, PRAZOPGTO)
        VALUES ({CodCliFor[i]}, {TipoCF[i]}, '{CodRepres[i]}', '{NomeFan[i]}', '{Cidade[i]}', '{Uf[i]}', '{CodMunicipio[i]}', {TipoPessoa[i]}, {Cobranc[i]}, '{PrazoPgto[i]}')
    """
    cursor.execute(sql)

print("Valores Adicionados com Sucesso a ClienFor!")


NUMPED =[]
NUMITEM =[]
CODPROD =[]
QTDE =[]
VALUNIT =[]
UNID =[]
ALIQICMS =[]
COMISSAO =[]
STICMS =[]
CFOP =[]
REDUCBASEICMS =[]

i=0
arq = open("PedidosItem.CSV")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
        # NUMPED.append(int(str(s[0].replace(".", ""))))
        # CODPROD.append(int(str(s[2].replace(".", ""))))
        NUMPED.append(str(s[0]))
        NUMITEM.append(int(s[1]))
        CODPROD.append(str(s[2].replace(".", "")))
        QTDE.append(str(s[3]))
        VALUNIT.append(str(s[4]))
        UNID.append(str(s[5]))
        ALIQICMS.append(str(s[6]))
        COMISSAO.append(str(s[7]))
        STICMS.append(int(s[8]))
        CFOP.append(str(s[9]))
        REDUCBASEICMS.append(str(s[10]))
    s = arq.readline().rstrip()
    i += 1
arq.close

sql = """
    CREATE TABLE IF NOT EXISTS PedidosItem
    (
    id integer primary key autoincrement,
    NUMPED string,
    NUMITEM integer,
    CODPROD string,
    QTDE string,
    VALUNIT string,
    UNID string,
    ALIQICMS string,
    COMISSAO string,
    STICMS integer,
    CFOP string,
    REDUCBASEICMS string
    )
"""
cursor.execute(sql)

for i in range(len(NUMITEM)):
    sql = f"""
        INSERT INTO PedidosItem (NUMPED, NUMITEM, CODPROD, QTDE, VALUNIT, UNID, ALIQICMS, COMISSAO, STICMS, CFOP, REDUCBASEICMS)
        VALUES ('{NUMPED[i]}', {NUMITEM[i]}, '{CODPROD[i]}', '{QTDE[i]}', '{VALUNIT[i]}', '{UNID[i]}','{ALIQICMS[i]}', '{COMISSAO[i]}', {STICMS[i]}, '{CFOP[i]}', '{REDUCBASEICMS[i]}')
    """
    cursor.execute(sql)

print("Valores Adicionados com Sucesso a PedidosItem!")



connector.commit()
cursor.close
connector.close()
