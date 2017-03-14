from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line



class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_string('''

 #: import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManagement:
    transition: FadeTransition()
    MainScreen:
    AnotherScreen:

<MainScreen>:
    name: "main"
    Button:
        on_release: app.root.current = "other"
        text: "Click Here to Draw"
        font_size: 50

<AnotherScreen>:
    name: "other"

    FloatLayout:
        Painter
        Button:
            color: 0,1,0,1
            font_size: 25
            size_hint: 0.2,0.1
            text: "Back Home"
            on_release: app.root.current = "main"
            pos_hint: {"right":1, "top":1}


 ''')


class MainApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()