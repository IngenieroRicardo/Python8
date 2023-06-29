import sqlite3

ltconn = sqlite3.connect("catalogos.db")
ltcursor = ltconn.cursor()

ltcursor.execute("select * from tiposdocumentos_terrestre;")
for row in ltcursor:
  print(row[0]," ",row[1])
ltcursor.close()
