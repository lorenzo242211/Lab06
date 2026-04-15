import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno = None
        self.brand = None
        self.retailer = None

    def riempiAnni(self):  # per menù a tendina servono due metodi
        # 1. Peschiamo i corsi dal Model (che chiama il DAO)
        anni = self._model.getAnni()
        # 2. Svuotiamo la tendina per sicurezza prima di riempirla
        self._view.ddAnni.options.clear()
        # AGGIUNGIAMO IL VALORE NULLO PER PRIMO
        self._view.ddAnni.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        # 3. Per ogni corso, creiamo un'Opzione Flet corretta
        for a in anni:
            self._view.ddAnni.options.append(
                ft.dropdown.Option(
                    key=a,  # Il dato utile per il database (es. '01QA')
                    text=a  # Quello che legge l'utente a schermo (es. 'Analisi')
                    # L'oggetto intero se serve dopo
                )
            )
        # 4. FONDAMENTALE: Diciamo alla grafica di aggiornarsi con le nuove opzioni
        self._view.update_page()

    def riempiBrand(self):  # per menù a tendina servono due metodi
        # 1. Peschiamo i corsi dal Model (che chiama il DAO)
        brand = self._model.getBrand()
        # 2. Svuotiamo la tendina per sicurezza prima di riempirla
        self._view.ddBrand.options.clear()
        # AGGIUNGIAMO IL VALORE NULLO PER PRIMO
        self._view.ddBrand.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        # 3. Per ogni corso, creiamo un'Opzione Flet corretta
        for b in brand:
            self._view.ddBrand.options.append(
                ft.dropdown.Option(
                    key=b,  # Il dato utile per il database (es. '01QA')
                    text=b  # Quello che legge l'utente a schermo (es. 'Analisi')
                    # L'oggetto intero se serve dopo
                )
            )

        # 4. FONDAMENTALE: Diciamo alla grafica di aggiornarsi con le nuove opzioni
        self._view.update_page()

    def riempiRetailer(self):  # per menù a tendina servono due metodi
            # 1. Peschiamo i corsi dal Model (che chiama il DAO)
            retailer = self._model.getRetailer()
            # 2. Svuotiamo la tendina per sicurezza prima di riempirla
            self._view.ddRetailer.options.clear()
            # AGGIUNGIAMO IL VALORE NULLO PER PRIMO
            self._view.ddRetailer.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
            # 3. Per ogni corso, creiamo un'Opzione Flet corretta
            for r in retailer:
                self._view.ddRetailer.options.append(
                    ft.dropdown.Option(key=r.Retailer_code,text=r.Retailer_name))
            # 4. FONDAMENTALE: Diciamo alla grafica di aggiornarsi con le nuove opzioni
            self._view.update_page()

    def sceltaAnni(self, e): self.anno = e.control.value;
    def sceltaBrand(self, e):
        self.brand = e.control.value
        print(self.brand) #prova
    def sceltaRetailer(self, e):
        self.retailer = e.control.value

   #stampa 5 migliori best sales per anno, retailer e brand, in base al ricavo: unitsale * quantity in daily sales, sorting in ordine decerscente
        #devo passargli il valore (value di anni, brand e retailer)
    def topVendite(self, e):
            # 1. Leggo i valori nudi e crudi dalle tendine
            anno = self._view.ddAnni.value
            brand = self._view.ddBrand.value
            retailer = self._view.ddRetailer.value

            # 2. LA TRADUZIONE FONDAMENTALE (Stringa vuota -> None) nei value abbiamo messo "" non none siccome è stringa
            if anno == "":
                anno = None
            if brand == "":
                brand = None
            if retailer == "":
                retailer = None

            # 3. Pulisco lo schermo dalle ricerche precedenti
            self._view.txt_result.controls.clear()

            # 4. Interrogo il Model con i dati puliti!
            vendite = self._model.getTopVendite(anno, brand, retailer)

            titolo = ft.Text(
                f"Stampo top 5 vendite - filtri selezionati: anno = {anno}   brand = {brand}   retailer = {retailer}  ",
                color="green")
            self._view.txt_result.controls.append(titolo)

            # 5. Gestisco la stampa
            if not vendite:  # Se la lista è vuota
                self._view.txt_result.controls.append(
                    ft.Text("Nessuna vendita trovata con questi filtri!", color="red")
                )
            else:
                for v in vendite:
                    # Aggiungi qui gli altri campi che vuoi stampare (brand, retailer, ricavo)
                    riga = ft.Text(f"Data: {v['data_vendita']}; Ricavo: {v['ricavo']}; Retailer: {v['retailer']}; Codice prodotto: {v['codice_prodotto']}")
                    self._view.txt_result.controls.append(riga)

            # 6. Aggiorno l'interfaccia
            self._view.update_page()

    #metodo per stampare statistiche, query identica cambia solo che non limito a 5 ma eredito tutti e li conto, conto statistiche

    def analisiVendite(self, e):
        pass
        #dalla query o ho lista enorme o mi faccio dare direttamente e analizzo i dati e roba passata da qua
