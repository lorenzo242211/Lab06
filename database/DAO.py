from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO():
    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # 1. Uso DISTINCT per prendere ogni anno una volta sola
        # 2. Uso 'AS anno' per dare un nome facile alla colonna
        # 3. (Opzionale) ORDER BY per averli in ordine cronologico
        query = """SELECT distinct YEAR(date) as anno FROM go_daily_sales ORDER by anno;""" #as anno implica creo dizionario associato

        cursor.execute(query)
        res = []

        # IL PEZZO MANCANTE: Leggiamo riga per riga dal cursore!
        for row in cursor:
            res.append(row["anno"]) #dizionario creato aggiungo alla lista riga anno

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # 1. Uso DISTINCT per prendere ogni anno una volta sola
        # 2. Uso 'AS anno' per dare un nome facile alla colonna
        # 3. (Opzionale) ORDER BY per averli in ordine cronologico
        query = """SELECT distinct Product_brand as prodo from go_products;"""

        cursor.execute(query)
        res = []

        # IL PEZZO MANCANTE: Leggiamo riga per riga dal cursore!
        for row in cursor:
            res.append(row["prodo"])  # dizionario creato aggiungo alla lista riga anno

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # 1. Ora usiamo SELECT * per prendere TUTTE le colonne necessarie a creare l'oggetto
        query = """SELECT * FROM go_retailers;"""

        cursor.execute(query)
        res = []

        for row in cursor:
            # LA MAGIA DEL **row!
            # Prende il dizionario 'row' e inietta tutti i valori direttamente nella Dataclass
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopVendite(a, b, r):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # La query fa letteralmente tutto il lavoro che avresti dovuto fare tu in Python!
        query = """
                    SELECT 
                        s.Date as data_vendita,
                        p.Product_brand as brand, 
                        s.Product_number as codice_prodotto,
                        r.Retailer_name as retailer,
                        (s.Unit_sale_price * s.Quantity) AS ricavo
                    FROM go_daily_sales s
                    JOIN go_products p ON s.Product_number = p.Product_number
                    JOIN go_retailers r ON s.Retailer_code = r.Retailer_code
                    WHERE 
                        YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
                        AND p.Product_brand = COALESCE(%s, p.Product_brand)
                        AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
                    ORDER BY ricavo DESC
                    LIMIT 999;
                """

        # Passiamo i 3 filtri. Se uno è None, COALESCE lo ignora e non filtra, fa direttamente quello che avrei voluto/dovuto fare
        cursor.execute(query, (a, b, r))

        res = []
        for row in cursor:
            # Per semplicità restituiamo direttamente il dizionario della riga
            res.append(row)

        cursor.close()
        cnx.close()
        print(res)
        return res