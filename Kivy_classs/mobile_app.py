from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainLayout=BoxLayout(orientation='horizontal')
        a = Button(text='Войти:')
        b = Label(text='Это текст')
        vl_01 = BoxLayout(orientation='horizontal')
        vl_01.add_widget(Button(text='Новый текст'))
        vl_01.add_widget(Button(text='Новый текст'))
        mainLayout.add_widget(a)
        mainLayout.add_widget(b)
        mainLayout.add_widget(vl_01)

        a.on_press = self.login
        self.add_widget(mainLayout)
    def login(self):
        self.manager.current='Логин'
        self.manager.transition.direction = 'up'


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainLayout=BoxLayout(orientation='horizontal')
        self.a = Button(text='Login:')
        self.b = TextInput()
        vl_01 = BoxLayout(orientation='horizontal')
        vl_01.add_widget(Button(text='Новый текст'))
        vl_01.add_widget(Button(text='Новый текст'))
        mainLayout.add_widget(self.a)
        mainLayout.add_widget(self.b)
        mainLayout.add_widget(vl_01)
        self.add_widget(mainLayout)
        self.a.on_press = self.login
    def login(self):
        if self.b.text == 'Приввт':
            self.a.text = self.b.text
        else:
            self.a.text = 'Неправильный пароль!!!'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='Главный экран'))
        sm.add_widget(LoginScreen(name='Логин'))
        return sm

MyApp().run()


