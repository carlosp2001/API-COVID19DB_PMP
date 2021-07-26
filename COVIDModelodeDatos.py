import sqlite3

class CovidDatos:
    def __init__(self):
        self.conn=sqlite3.connect("covid.db")
        cursor=self.conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS covid (        
                        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                        pais text NOT NULL,
                        idpais text NOT NULL,
                        casosconfirmados INTEGER NOT NULL,
                        casoscriticos INTEGER NOT NULL,
                        muertes INTEGER NOT NULL
                                       );'''
                       )
        self.conn.commit()
    def agregarCovidInfo(self, pais,idpais,casosconfirmados,casoscriticos,muertes):
        cursor=self.conn.cursor()
        cursor.execute('''INSERT INTO covid(pais,idpais,casosconfirmados,casoscriticos,muertes)
                        VALUES(?,?,?,?,?);''',(pais,idpais,casosconfirmados,casoscriticos,muertes))
        self.conn.commit()

    def MostrarTodalaInformacion(self):
        cursor=self.conn.cursor()
        cursor.execute('''SELECT * FROM covid;''')
        resultado=cursor.fetchall()
        self.conn.commit()
        print('%-20s %-20s %-20s %-20s %-20s ' % (
        "Pais", "Codigo del Pais", "Casos Confirmados", "Casos Criticos", "Muertes"))
        print("-" * 1000)
        for record in resultado:
            print('%-20s %-20s %-20s %-20s %-20s' % (record[1], record[2], record[3], record[4], record[5]))

    def Mostrarinformaciondepais(self,pais):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM covid where pais=?''',(pais,))
        resultado = cursor.fetchall()
        self.conn.commit()
        print('%-20s %-20s %-20s %-20s %-20s ' % (
        "Pais", "Codigo del Pais", "Casos Confirmados", "Casos Criticos", "Muertes"))
        print("-" * 1000)
        for record in resultado:
            print('%-20s %-20s %-20s %-20s %-20s' % (record[1], record[2], record[3], record[4], record[5]))













