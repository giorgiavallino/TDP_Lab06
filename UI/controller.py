import flet as ft

class Controller:

    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model
        # Altri elementi
        self._ddRetailerValue = None

    def fillDDAnno(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddAnno.options.append(ft.dropdown.Option(anno))

    def fillDDBrand(self):
        brands = self._model.getBrand()
        for brand in brands:
            self._view.ddBrand.options.append(ft.dropdown.Option(brand))

    def fillDDRetailer(self):
        retailers = self._model.getRetailer()
        for retailer in retailers:
            self._view.ddRetailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                    text=retailer.retailer_name,
                                                                    data=retailer,
                                                                    on_click=self._readRetailer))

    def _readRetailer(self, e):
        self._ddRetailerValue = e.control.data