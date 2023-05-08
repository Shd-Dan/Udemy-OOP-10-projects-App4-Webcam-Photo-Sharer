from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget


# run() is the method of inherited from App
MainApp().run()
