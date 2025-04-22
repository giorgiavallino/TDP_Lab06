from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT(YEAR(gds.Date))
                    FROM go_daily_sales gds"""
            cursor.execute(query,)
            for row in cursor:
                risultato.append(row[0])
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT(gp.Product_brand)
                    FROM go_products gp"""
            cursor.execute(query, )
            for row in cursor:
                risultato.append(row[0])
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM go_retailers"""
            cursor.execute(query, )
            for row in cursor:
                risultato.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
            cursor.close()
            cnx.close()
            return risultato