from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from create_data import crearImagenes
from faceRecognition import reconocer

class IndexScreen(Screen):
    
    pass

class RegisterScreen(Screen):
    
    def registrarImagenes(self, carpeta):
        crearImagenes(carpeta)

class HomeScreen(Screen):
    
    def login(self):
        entrar = reconocer()
        print(entrar)

class ScreenManager(ScreenManager):
    pass

kv = Builder.load_file("tpi.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()