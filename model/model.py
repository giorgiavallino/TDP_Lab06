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