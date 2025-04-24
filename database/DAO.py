from database.DB_connect import DBConnect
from model.products import Product
from model.retailer import Retailer
from model.sales import Sale

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
                    FROM go_daily_sales gds
                    ORDER BY YEAR(gds.Date)"""
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
                    FROM go_products gp
                    ORDER BY gp.Product_brand"""
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
            query = """SELECT gr.*
                    FROM go_retailers gr
                    ORDER BY gr.Retailer_name"""
            cursor.execute(query, )
            for row in cursor:
                risultato.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def searchVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor()
            query = """SELECT gds.*, gds.Quantity * gds.Unit_sale_price as Ricavo
                    FROM go_daily_sales gds,  go_products gp
                    WHERE gds.Product_number = gp.Product_number
                    AND YEAR(gds.Date) = COALESCE(%s, YEAR(gds.Date))
                    AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
                    AND gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                    ORDER BY Ricavo DESC"""
            cursor.execute(query, (anno, brand, retailer,))
            for row in cursor:
                risultato.append(Sale(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getNumeroCoinvolti(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor()
            query = """SELECT COUNT(DISTINCT(gds.Retailer_code)), COUNT(DISTINCT(gds.Product_number))
                    FROM go_daily_sales gds,  go_products gp
                    WHERE gds.Product_number = gp.Product_number
                    AND YEAR(gds.Date) = COALESCE(%s, YEAR(gds.Date))
                    AND gp.Product_brand = coalesce(%s, gp.Product_brand)
                    AND gds.Retailer_code = coalesce(%s, gds.Retailer_code)"""
            cursor.execute(query, (anno, brand, retailer,))
            for row in cursor:
                risultato.append(row)
            cursor.close()
            cnx.close()
            return risultato