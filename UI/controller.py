import flet as ft

class Controller:

    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model
        # Altri elementi
        self._ddRetailerValueText = None
        self._ddRetailerValueKey = None

    def fillDDAnno(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddAnno.options.append(ft.dropdown.Option(anno))

    def fillDDBrand(self):
        brands = self._model.getBrand()
        for brand in brands:
            self._view.ddBrand.options.append(ft.dropdown.Option(brand))

    def fillDDRetailer(self):
        self._view.ddRetailer.options.append(ft.dropdown.Option(key="None",
                                                                text="Nessun filtro",
                                                                on_click=self.readRetailer))
        retailers = self._model.getRetailer()
        for retailer in retailers:
            self._view.ddRetailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                    text=retailer.retailer_name,
                                                                    data=retailer,
                                                                    on_click=self.readRetailer))

    def readRetailer(self, e):
        self._ddRetailerValueText = e.control.text
        self._ddRetailerValueKey = e.control.key

    def searchTopVendite(self, e):
        self._view.lvTxtOut.controls.clear()
        anno = self._view.ddAnno.value
        if anno == None:
            self._view.create_alert("Selezionare un'opzione del menù Anno!")
            self._view.update_page()
            return
        if anno == "Nessun filtro":
            anno = None
        brand = self._view.ddBrand.value
        if brand is None:
            self._view.create_alert("Selezionare un'opzione del menù Brand!")
            self._view.update_page()
            return
        if brand == "Nessun filtro":
            brand = None
        retailerText = self._ddRetailerValueText
        retailerKey = self._ddRetailerValueKey
        if retailerText is None:
            self._view.create_alert("Selezionare un'opzione del menù Retailer!")
            self._view.update_page()
            return
        if retailerText == "Nessun filtro":
            retailerKey = None
        risultato = self._model.searchTopVendite(anno, brand, retailerKey)
        if len(risultato) == 0:
            self._view.lvTxtOut.controls.append(ft.Text(f"Non sono state registrate vendite con i filtri impostati."))
            self._view.update_page()
            return
        for elemento in risultato:
            self._view.lvTxtOut.controls.append(ft.Text(f"{elemento}"))
        self._view.update_page()

    def analizzaVendite(self, e):
        self._view.lvTxtOut.controls.clear()
        anno = self._view.ddAnno.value
        if anno == None:
            self._view.create_alert("Selezionare un'opzione del menù Anno!")
            self._view.update_page()
            return
        if anno == "Nessun filtro":
            anno = None
        brand = self._view.ddBrand.value
        if brand is None:
            self._view.create_alert("Selezionare un'opzione del menù Brand!")
            self._view.update_page()
            return
        if brand == "Nessun filtro":
            brand = None
        retailerText = self._ddRetailerValueText
        retailerKey = self._ddRetailerValueKey
        if retailerText is None:
            self._view.create_alert("Selezionare un'opzione del menù Retailer!")
            self._view.update_page()
            return
        if retailerText == "Nessun filtro":
            retailerKey = None
        ricavo, numeroVendite = self._model.analizzaVendite_01(anno, brand, retailerKey)
        if numeroVendite == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Non sono state registrate vendite con i filtri impostati."))
            self._view.update_page()
            return
        numeriCoinvolti = self._model.analizzaVendite_02(anno, brand, retailerKey)
        self._view.lvTxtOut.controls.append(ft.Text(f"Statistiche vendite\n"
                                                    f"Giro d'affari: {ricavo}\n"
                                                    f"Numero vendite: {numeroVendite}\n"
                                                    f"Numero retailers coinvolti: {numeriCoinvolti[0][0]}\n"
                                                    f"Numero prodotti coinvolti: {numeriCoinvolti[0][1]}"))
        self._view.update_page()