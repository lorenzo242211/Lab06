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

    def getTopVendite(self, anno, brand, retailer):
        return DAO.getTopVendite(anno, brand, retailer)


if __name__ == '__main__':
    m = Model()
    lista = m.getAnni()
    for a in lista:
        print(a)

    brand = m.getBrand()
    for numero, b  in enumerate(brand):
        print(f"{numero+1}: {b}")

    retailer = m.getRetailer()
    print(retailer)
    for numero, r in enumerate(retailer):
        print(f"{numero+1}: {r}")


