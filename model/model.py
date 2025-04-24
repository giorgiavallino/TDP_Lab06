from database.DAO import DAO

class Model:

    def __init__(self):
        pass

    def getAnni(self):
        return DAO.getAnni()

    def getBrand(self):
        return DAO.getBrand()

    def getRetailer(self):
        return DAO.getRetailer()

    def searchTopVendite(self, anno, brand, retailer):
        vendite = DAO.searchVendite(anno, brand, retailer)
        top_vendite = vendite[0:5]
        return top_vendite

    def analizzaVendite_01(self, anno, brand, retailer):
        vendite = DAO.searchVendite(anno, brand, retailer)
        ricavo_totale = sum([vendita.ricavo for vendita in vendite])
        return ricavo_totale, len(vendite)

    def analizzaVendite_02(self, anno, brand, retailer):
        return DAO.getNumeroCoinvolti(anno, brand, retailer)