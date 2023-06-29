import sqlite3

ltconn = sqlite3.connect("catalogos.db")
ltcursor = ltconn.cursor()

#ltcursor.execute("DELETE FROM tiposdocumentos_terrestre WHERE CodigoTipoDocumentoIdentidad=1000")
ltcursor.execute("INSERT INTO tiposdocumentos_terrestre VALUES(1000, 'PASAPORTE PROVICIONAL');")
ltconn.commit()
ltcursor.close()
