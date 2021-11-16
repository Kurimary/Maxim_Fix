from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
#КАЖДЫЙ ЭКРАН - ОТДЕЛЬНЫЙ КЛАСС
class main_Window(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        #Создаем все необходимые виджеты
        text = Label(text='Выбери экран!')
        but1 = Button(text='1')
        but2 = Button(text='2')
        but3 = Button(text='3')
        but4 = Button(text='4')
        layut = BoxLayout(orientation='vertical', spacing = 15, )
        layut1 = BoxLayout(orientation='horizontal')
        layut.add_widget(but1)
        layut.add_widget(but2)
        layut.add_widget(but3)
        layut.add_widget(but4)
        layut1.add_widget(text)
        layut1.add_widget(layut)
        self.add_widget(layut1)

        but1.on_press = self.next
        but2.on_press = self.next2

    def next(self):
        self.manager.transition.direction = 'up'  #'left' 'up' 'right'#Указываем только 1 вариант из 4
        self.manager.current = 'Второе окно'
    def next2(self):
        self.manager.transition.direction = 'right'  #'left' 'up' 'right'#Указываем только 1 вариант из 4
        self.manager.current = 'Третье окно'



class second_Window(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #Создаем все необходимые виджеты


        # pos_hint = {'center_x' , 'center_y', 'right', 'left'}
        # size_hint = (x,y)  Где х y числа от 0 до 1
        but2 = Button(text='Просто кнопка', size_hint=(0.5, 0.5), pos_hint={'left': 0})
        but1 = Button(text='Назад', size_hint=(0.5, 0.5), pos_hint={'right': 1})
        layout.add_widget(but1)
        layout.add_widget(but2)
        but1.on_press = self.next
        self.add_widget(layout)#ОДНА ЕДИНСТВЕННАЯ
    def next(self):
        self.manager.transition.direction = 'down'  #'left' 'up' 'right'#Указываем только 1 вариант из 4
        self.manager.current = 'Главное окно'




class third_Window(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        self.label = Label(text='Выбор 2', )
        vl.add_widget(self.label)
        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.label1 = Label(text='Введите пароль', )
        self.textinput = TextInput(multiline=False)
        hl_0.add_widget(self.label1)
        hl_0.add_widget(self.textinput)
        vl.add_widget(hl_0)
        self.btn1 = Button(text='Back')
        btn2 = Button(text='Ввод текста')
        hl_1 = BoxLayout(size_hint=(0.7, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        hl_1.add_widget(self.btn1)
        hl_1.add_widget(btn2)
        vl.add_widget(hl_1)
        self.add_widget(vl)
        btn2.on_press = self.change_label
        self.btn1.on_press = self.next

    def change_label(self):
        self.label.text = self.textinput.text + ' да, да, ты нажал на кнопку!'
        self.btn1.text = 'Добро пожаловать Username!'
    def next(self):
        self.manager.transition.direction = 'left'  #'left' 'up' 'right'#Указываем только 1 вариант из 4
        self.manager.current = 'Главное окно'

# Здесь НЕ настроены Лэйауты, расположение элементов, кнопки. Сделайте сами
class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout()
        a = 'START' + 'Выбор: 3' * 200
        self.label = Label(text=a)
        self.scroll = ScrollView(size_hint=(1,1))
        self.scroll.add_widget(self.label)
        self.label.bind(size=self.resize)

    def resize(self):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.text_size[1]

#В КЛАССЕ ПРИЛОЖЕНИЯ - ТОЛЬКО ScreenManager
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(main_Window(name='Главное окно'))
        sm.add_widget(second_Window(name='Второе окно'))
        sm.add_widget(third_Window(name='Третье окно'))
        return sm
MyApp().run()
#Создаем объект класса MyApp
#Вызываем метод run()


