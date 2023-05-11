"""image_files directory to be created in case pulling project from Github repo"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
# to copy in Clipboard import a class Clipboard
from kivy.core.clipboard import Clipboard
import time
# to open link in browser
import webbrowser

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
        # self makes filepath an attribute of CameraScreen Instance
        self.filepath = f'image_files/{current_time}.png'
        self.ids.camera.export_to_png(self.filepath)

        # Accessing manager attribute from Screen instance
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message = "Create a Link First"

    def create_link(self):
        """ Accesses the photo filepath, uploads it to the web, and inserts
        the link in the Label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        # Instance of FileSharer class
        filesharer = FileSharer(filepath=file_path)
        # returns an URL
        self.url = filesharer.share()
        # Get access to label and assigns Widget instance text attribute with url string address
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy link to the clipboard available for pasting"""
        # copy() is a class method no need for an instance
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Open link with default browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        # Important notice! 'play' attribute of Camera by default is False.
        return RootWidget()


# run() is the method of inherited from App
MainApp().run()
