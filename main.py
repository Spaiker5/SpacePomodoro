from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    MenuScreen:
    SpaceScreen:
    DataScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Fly'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'space'
    MDRectangleFlatButton:
        text: 'Statistic'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'data'

<SpaceScreen>:
    name: 'space'
    MDLabel:
        text: 'Fly!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<DataScreen>:
    name: 'data'
    MDLabel:
        text: 'Statistics'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass


class SpaceScreen(Screen):
    pass


class DataScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SpaceScreen(name='space'))
sm.add_widget(DataScreen(name='data'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
