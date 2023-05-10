from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

from filesharer import FileSharer

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        """Starts camera and changes Button text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """ids is a link to an attribute of kv file
            export_to_png() is inherited method of Screen kivy class.
            strftime() is method of time library used to create a unique name
        """
        current_time = time.strftime('%Y%m%d-%H%M%S')
        filepath = f'image_files/{current_time}.png'
        self.ids.camera.export_to_png(filepath)

        # Accessing manager attribute from Screen instance
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath

class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        # Important notice! 'play' attribute of Camera by default is False.
        return RootWidget()


# run() is the method of inherited from App
MainApp().run()
