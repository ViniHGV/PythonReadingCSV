import sqlite3

connector = sqlite3.connect("Loja.db")
cursor = connector.cursor()

CodRrepres = []
TipoPess = []
NomeFan = []
ComissaoBase = []

tabelas = ['Repres', 'FornClien', 'PedidosItem', 'Produtos', 'Pedidos']

for tabela in tabelas:
    sql = f"DROP TABLE IF EXISTS {tabela};"
    cursor.execute(sql)

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
    CODREPRES INTEGER PRIMARY KEY,
    TIPOPESS TEXT,
    NOMEFAN TEXT,
    COMISSAOBASE NUMERIC
    )
"""
cursor.execute(sql)

print("Tabela Repres Criada 🚀")

for i in range(len(CodRrepres)):
    sql = """
        INSERT INTO Repres (CODREPRES, TIPOPESS, NOMEFAN, COMISSAOBASE)
        VALUES (?,?,?,?)
    """
    cursor.execute(sql, (CodRrepres[i], TipoPess[i], NomeFan[i], ComissaoBase[i]))

print("Valores Adicionados com Sucesso a Repres!")

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
    CODCLIFOR INTEGER PRIMARY KEY,
    TIPOCF INTEGER,
    CODREPRES TEXT,
    NOMEFAN TEXT,
    CIDADE TEXT,
    UF TEXT,
    CODMUNICIPIO TEXT,
    TIPOPESSOA INTEGER,
    COBRBANC INTEGER,
    PRAZOPGTO TEXT
    )
"""
cursor.execute(sql)

for i in range(len(CodCliFor)):
    sql = f"""
        INSERT INTO FornClien (CODCLIFOR, TIPOCF, CODREPRES, NOMEFAN, CIDADE, UF, CODMUNICIPIO, TIPOPESSOA, COBRBANC, PRAZOPGTO)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """
    cursor.execute(sql, (CodCliFor[i], TipoCF[i], CodRepres[i], NomeFan[i], Cidade[i], Uf[i], CodMunicipio[i], TipoPessoa[i], Cobranc[i], PrazoPgto[i]))

print("Valores Adicionados com Sucesso a ClienFor!")


NUMPED = []
NUMITEM = []
CODPROD = []
QTDE = []
VALUNIT = []
UNID = []
ALIQICMS = []
COMISSAO = []
STICMS = []
CFOP = []
REDUCBASEICMS = []

i=0
arq = open("PedidosItem.CSV")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NUMPED TEXT,
    NUMITEM INTEGER,
    CODPROD TEXT,
    QTDE TEXT,
    VALUNIT TEXT,
    UNID TEXT,
    ALIQICMS TEXT,
    COMISSAO TEXT,
    STICMS INTEGER,
    CFOP TEXT,
    REDUCBASEICMS TEXT
    )
"""
cursor.execute(sql)

for i in range(len(NUMITEM)):
    sql = f"""
        INSERT INTO PedidosItem (NUMPED, NUMITEM, CODPROD, QTDE, VALUNIT, UNID, ALIQICMS, COMISSAO, STICMS, CFOP, REDUCBASEICMS)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """
    cursor.execute(sql, (NUMPED[i], NUMITEM[i], CODPROD[i], QTDE[i], VALUNIT[i], UNID[i],ALIQICMS[i], COMISSAO[i], STICMS[i], CFOP[i], REDUCBASEICMS[i]))

print("Valores Adicionados com Sucesso a PedidosItem!")


CODPROD = []
NOMEPROD = []
CODFORNE = []
UNIDADE = []
ALIQICMS = []
VALCUSTO = []
VALVENDA = []
QTDEMIN = []
QTDEESTQ = []
GRUPO = []
CLASSESTQ = []
COMISSAO = []
PESOBRUTO = []

i=0
arq = open("Produtos.CSV")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
        CODPROD.append(int(str(s[0].replace(".", ""))))
        NOMEPROD.append(str(s[1]))
        CODFORNE.append(str(s[2]))
        UNIDADE.append(int(s[3]))
        ALIQICMS.append(str(s[4]))
        VALCUSTO.append(str(s[5]))
        VALVENDA.append(str(s[6]))
        QTDEMIN.append(str(s[7]))
        QTDEESTQ.append(str(s[8]))
        GRUPO.append(int(s[9]))
        CLASSESTQ.append(str(s[10]))
        COMISSAO.append(str(s[11]))
        PESOBRUTO.append(str(s[12]))
    s = arq.readline().rstrip()
    i += 1
arq.close

sql = """
    CREATE TABLE IF NOT EXISTS Produtos
    (
    CODPROD INTEGER PRIMARY KEY,
    NOMEPROD TEXT,
    CODFORNE TEXT,
    UNIDADE TEXT,  
    ALIQICMS TEXT,
    VALCUSTO TEXT,
    VALVENDA TEXT,
    QTDEMIN TEXT,
    QTDEESTQ INTEGER, 
    GRUPO INTEGER,
    CLASSESTQ TEXT,
    COMISSAO TEXT,
    PESOBRUTO TEXT 
    )
"""
cursor.execute(sql)

for i in range(len(CODPROD)):
    sql = """
        INSERT INTO Produtos (CODPROD, NOMEPROD, CODFORNE, UNIDADE, ALIQICMS, VALCUSTO, VALVENDA, QTDEMIN, QTDEESTQ, GRUPO, CLASSESTQ, COMISSAO, PESOBRUTO)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (CODPROD[i], NOMEPROD[i], CODFORNE[i], UNIDADE[i], ALIQICMS[i], VALCUSTO[i], VALVENDA[i], QTDEMIN[i], QTDEESTQ[i], GRUPO[i], CLASSESTQ[i], COMISSAO[i], PESOBRUTO[i]))


print("Valores Adicionados com Sucesso a Produtos!")


NUMPED =[]
DATAPED	 =[]
HORAPED =[]
CODCLIEN =[]
ES =[]
FINALIDNFE =[]
SITUACAO =[]
PESO =[]
PRAZOPGTO =[]
VALORPRODS =[]
VALORDESC =[]
VALOR =[]
VALBASEICMS =[]
VALICMS =[]
COMISSAO =[]


i=0
arq = open("Pedidos.CSV")
s = arq.readline().rstrip()
while s != "":
    s = s.split(";")
    if i > 0:
        NUMPED.append(int(str(s[0].replace(".", ""))))
        DATAPED.append(str(s[1]))
        HORAPED.append(str(s[2]))
        CODCLIEN.append(str(s[3]))
        ES.append(str(s[4]))
        FINALIDNFE.append(int(s[5]))
        SITUACAO.append(int(s[6]))
        PESO.append(str(s[7]))
        PRAZOPGTO.append(int(s[8]))
        VALORPRODS.append(str(s[9]))
        VALORDESC.append(str(s[10]))
        VALOR.append(str(s[11]))
        VALBASEICMS.append(str(s[12]))
        VALICMS.append(str(s[13]))
        COMISSAO.append(str(s[14]))
    s = arq.readline().rstrip()
    i += 1
arq.close

sql = """
   CREATE TABLE IF NOT EXISTS Pedidos (
    NUMPED INTEGER PRIMARY KEY,
    DATAPED TEXT,
    HORAPED TEXT,
    CODCLIEN TEXT,
    ES TEXT,
    FINALIDNFE INTEGER,
    SITUACAO INTEGER,
    PESO TEXT,
    PRAZOPGTO INTEGER,
    VALORPRODS TEXT,
    VALORDESC TEXT,
    VALOR TEXT,
    VALBASEICMS TEXT,
    VALICMS TEXT,
    COMISSAO TEXT
);
"""
cursor.execute(sql)

for i in range(len(NUMPED)):
    sql = """
        INSERT INTO Pedidos (NUMPED, DATAPED, HORAPED, CODCLIEN, ES, FINALIDNFE, SITUACAO, PESO, PRAZOPGTO, VALORPRODS, VALORDESC, VALOR, VALBASEICMS, VALICMS, COMISSAO)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (
        NUMPED[i],
        DATAPED[i],
        HORAPED[i],
        CODCLIEN[i],
        ES[i],
        FINALIDNFE[i],
        SITUACAO[i],
        PESO[i],
        PRAZOPGTO[i],
        VALORPRODS[i],
        VALORDESC[i],
        VALOR[i],
        VALBASEICMS[i],
        VALICMS[i],
        COMISSAO[i]
    ))


print("Valores Adicionados com Sucesso a Pedidos!")


connector.commit()
cursor.close
connector.close()
