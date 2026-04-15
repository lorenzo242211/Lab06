import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06 - Analisi Vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None
        self.txt_container = None
        self.ddAnni = None
        self.ddBrand = None
        self.ddRetailer = None
        self.btnTop = None
        self.btnAnalisi = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)
        #Riga1
        self.ddAnni = ft.Dropdown(label="anno", on_change = self._controller.sceltaAnni)
        self._controller.riempiAnni()
        self.ddBrand = ft.Dropdown(label="brand", on_change = self._controller.sceltaBrand)
        self._controller.riempiBrand()
        self.ddRetailer = ft.Dropdown(label="retailer", expand=True, on_change = self._controller.sceltaRetailer)
        self._controller.riempiRetailer()
        row1 = ft.Row([self.ddAnni, self.ddBrand, self.ddRetailer])
        self.btnTop = ft.ElevatedButton(text="Top Vendite", on_click= self._controller.topVendite) #avvia la ricerca con attuali filtri inseriti nei menu sopra
        self.btnAnalisi = ft.ElevatedButton(text="Analisi Vendite", on_click= None)
        row2 = ft.Row([self.btnTop, self.btnAnalisi], alignment= MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self._page.add(row1, row2)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


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
