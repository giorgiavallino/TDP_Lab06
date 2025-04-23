import flet as ft

class View(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        # Page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # Graphical elements
        self._title = None
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        self.btnTopVendite = None
        self.btnAnalizzaVendite = None
        self.lvTxtOut = None

    def load_interface(self):
        # Title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)
        # Altri elementi grafici
        self.ddAnno = ft.Dropdown(label="Anno",
                                  hint_text="Selezionare l'anno",
                                  options=[ft.dropdown.Option("Nessun filtro")],
                                  width=150)
        self._controller.fillDDAnno()
        self.ddBrand = ft.Dropdown(label="Brand",
                                   hint_text="Selezionare il brand",
                                   options=[ft.dropdown.Option("Nessun filtro")],
                                   width=250)
        self._controller.fillDDBrand()
        self.ddRetailer = ft.Dropdown(label="Retailer",
                                      hint_text="Selezionare il retailer",
                                      options=[ft.dropdown.Option("Nessun filtro")],
                                      width=500)
        self._controller.fillDDRetailer()
        self.btnTopVendite = ft.ElevatedButton(text="Top vendite",
                                               on_click=self._controller.searchTopVendite)
        self.btnAnalizzaVendite = ft.ElevatedButton(text="Analizza vendite")
        self.lvTxtOut = ft.ListView(expand=True)
        row_01 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer],
                        alignment=ft.MainAxisAlignment.CENTER)
        row_02 = ft.Row([self.btnTopVendite, self.btnAnalizzaVendite],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row_01, row_02, self.lvTxtOut)
        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
