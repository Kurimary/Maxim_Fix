#не забудь импортировать необходимые элементы!
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn1 = Button(text = '1')
        btn2 = Button(text = '2')
        btn3 = Button(text = '3')
        btn4 = Button(text = '4')
        lbl = Label(text = 'Выбери экран')
        MainLayout = BoxLayout(orientation = 'horizontal')
        Layout = BoxLayout(orientation = 'vertical')
        MainLayout.add_widget(lbl)
        MainLayout.add_widget(Layout)
        Layout.add_widget(btn1)
        Layout.add_widget(btn2)
        Layout.add_widget(btn3)
        Layout.add_widget(btn4)
        self.add_widget(MainLayout)
        btn1.on_press = self.next1
        btn2.on_press = self.next2
        btn3.on_press = self.next3
        #btn4.on_press = self.next4
    def next1(self):
        self.manager.current = 'Scr1'
    def next2(self):
        self.manager.current = 'Scr2'
    def next3(self):
        self.manager.current = 'Scr3'
    #def next4(self):
       # self.manager.current = 'Scr4'

class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        MainLayout1 = BoxLayout(orientation = 'vertical', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btnScr11 = Button(text = 'Выбор: 1', size_hint=(0.5, 0.5), pos_hint={'left': 0})
        btnScr12 = Button(text = 'Назад', size_hint=(0.5, 0.5), pos_hint={'right': 1})
        MainLayout1.add_widget(btnScr11)
        MainLayout1.add_widget(btnScr12)
        self.add_widget(MainLayout1)
        btnScr12.on_press = self.next12
    def next12(self):
        self.manager.current = 'MainScr'

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        MainLayout2 = BoxLayout(orientation = 'vertical')
        self.lbl21 = Label(text = 'Выбор: 2', font_size='30sp')
        self.lbl22 = Label(text = 'Введите пароль:')
        self.Input21 = TextInput()
        btnScr21 = Button(text = 'ОК!')
        self.btnScr22 = Button(text = 'Назад')
        Layout21 = BoxLayout(orientation = 'horizontal', size_hint=(0.8, None), height = '30sp')
        Layout22 = BoxLayout(orientation = 'horizontal', pos_hint={'center_x': 0.5}, size_hint=(0.7, 0.2), )
        MainLayout2.add_widget(self.lbl21)
        Layout22.add_widget(btnScr21)
        Layout22.add_widget(self.btnScr22)
        Layout21.add_widget(self.lbl22)
        Layout21.add_widget(self.Input21)
        MainLayout2.add_widget(Layout21)
        MainLayout2.add_widget(Layout22)
        self.add_widget(MainLayout2)
        self.btnScr22.on_press = self.next21
        btnScr21.on_press = self.change_label
    def change_label(self):
        self.lbl21.text = self.Input21.text + ' да, да, ты нажал на кнопку!'
        self.btnScr22.text = 'Добро пожаловать Username!'
    def next21(self):
        self.manager.current = 'MainScr'

class ScreenThree(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        MainLayout3 = BoxLayout(orientation = 'vertical')
        lbl31 = Label(text = 'Login:')
        lbl32 = Label(text = 'Password:')
        self.Input31 = TextInput()
        self.Input32 = TextInput()
        btnScr31 = Button(text = 'Home')
        btnScr32 = Button(text = 'Войти')
        btnScr33 = Button(text = 'Забыл пароль')
        Layout31 = BoxLayout(orientation = 'horizontal', size_hint=(0.8, None), height = '30sp', pos_hint={'center_x': 0.5, 'center_y': 0})
        Layout32 = BoxLayout(orientation = 'horizontal', size_hint=(0.8, None), height = '30sp', pos_hint={'center_x': 0.5, 'center_y': 0})
        Layout33 = BoxLayout(orientation = 'horizontal', pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.7, None))
        Layout31.add_widget(lbl31)
        Layout31.add_widget(self.Input31)
        Layout32.add_widget(lbl32)
        Layout32.add_widget(self.Input32)
        Layout33.add_widget(btnScr31)
        Layout33.add_widget(btnScr32)
        Layout33.add_widget(btnScr33)
        MainLayout3.add_widget(Layout31)
        MainLayout3.add_widget(Layout32)
        MainLayout3.add_widget(Layout33)
        self.add_widget(MainLayout3)
        btnScr31.on_press = self.next31
    def next31(self):
        self.manager.current = 'MainScr'

class MyClass(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'MainScr'))
        sm.add_widget(ScreenOne(name='Scr1'))
        sm.add_widget(ScreenTwo(name='Scr2'))
        sm.add_widget(ScreenThree(name='Scr3'))
        return sm

obj = MyClass()
obj.run()
