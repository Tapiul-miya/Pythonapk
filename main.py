from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.utils.set_bars_colors import set_bars_colors

class SampleApp(MDApp):

    def __init__(self, **kwargs) -> None:
        super(SampleApp, self).__init__(**kwargs)
        # 'Darkblue' palette nei, standard 'Blue' use kora hoyeche
        self.theme_cls.primary_palette = "Blue" 

    def build(self) -> MDScreen:
        # KV text string-e direct root references call kora hoyeche
        self.appKv = """
MDScreen:
    MDButton:
        style: 'tonal'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            app.apply_styles("Dark") if app.theme_cls.theme_style == "Light" else app.apply_styles("Light")

        MDButtonText:
            text: 'Hello, World!'
"""
        AppScreen = Builder.load_string(self.appKv)
        self.apply_styles("Light")
        return AppScreen

    def apply_styles(self, style: str = "Light") -> None:
        self.theme_cls.theme_style = style
        
        # v2.0.0 standard onujayi self.theme_cls.surface_color hobe
        status_color = nav_color = self.theme_cls.surface_color
        Window.clearcolor = status_color
        
        if style == "Light":
            icon_style = "Dark"
        else:
            icon_style = "Light"
            
        self.set_bars_colors(status_color, nav_color, icon_style)

    def set_bars_colors(self, status_color: list[float] = [1.0, 1.0, 1.0, 1.0], 
                        nav_color: list[float] = [1.0, 1.0, 1.0, 1.0], 
                        style: str = "Dark") -> None:
        set_bars_colors(
            status_color,  # status bar bg color
            nav_color,     # navigation bar bg color
            style,         # icons style ('Dark' or 'Light')
        )

if __name__ == "__main__":
    SampleApp().run()
