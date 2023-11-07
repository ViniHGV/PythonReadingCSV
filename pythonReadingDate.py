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
while s != '':
    s = s.split(';')    
    CodRrepres.append(s[0])
    TipoPess.append(str(s[1]))
    NomeFan.append(str(s[2]))
    ComissaoBase.append(s[3])
    # CodRrepres.append(int(s[0]))
    # TipoPess.append(str(s[1]))
    # NomeFan.append(str(s[2]))
    # ComissaoBase.append(float(s[3]))
    s = arq.readline().rstrip()    
arq.close

# sql = '''
#     CREATE TABLE IF NOT EXISTS Repres
#     (
#     CODREPRES integer primary key,
#     TIPOPESS string,
#     NOMEFAN stirng,
#     COMISSAOBASE numeric
#     )
# '''
# cursor.execute(sql)

# print("Tabela Repres Criada 🚀")

# for i in range(len(CODREPRES)):
#     sql = f'''
#         INSERT INTO Repres (CODREPRES, TIPOPESS, NOMEFAN, COMISSAOBASE)
#         VALUES ({CODREPRES[i]}, '{TIPOPESS[i]}', '{NOMEFAN[i]}', {COMISSAOBASE[i]})
#     '''
    # cursor.execute(sql)

print("Valores Adicionados com Sucesso!")


connector.commit()
cursor.close
connector.close()

        
    
