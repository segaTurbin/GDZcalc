from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang.builder import Builder
import math
# Создаём экранную клавиатуру
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Задаём размер окна с помощью модуля Window
# Window.size = ()
Window.size = (480, 853)

KV = '''
<ItemLabel@Label>
    font_size: '25sp'
    halign: 'center'
    valign: 'middle'
    text_size: self.size

<Container>
    rows: 3
# Присваиваем значения ключей
    text_input: text_input
    p_max_drop: p_max_drop
    p_cont_exit: p_cont_exit
    delta_t: delta_t
    time_exit: time_exit
    total_time: total_time
    return_time: return_time

    AnchorLayout:
        size_hint: 1, 0.15
        padding: [20, 10, 20, 0]
        TextInput:
            id: text_input
            multiline: False
            font_size: '45sp'
            input_type: 'number'
            input_filter: 'int'
            hint_text: "для баллона 6,8 л"
            padding: [20, 10, 20, 0]
            halign: 'center'
            valign: 'middle'


    GridLayout:
        cols: 2

        BoxLayout:
            orientation: 'vertical'
            padding: [30, 0, 0, 0]
            ItemLabel:
                text: 'P max пад ='

            ItemLabel:
                text: 'P конт. вых ='

            ItemLabel:
                text: 'Δ T ='

            ItemLabel:
                text: 'T выхода  =  T вкл  +'

            ItemLabel:
                text: 'T общее ='

            ItemLabel:
                text: 'T возвр = T вкл +'


        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.5, 1
            ItemLabel:
                id: p_max_drop
                text: '0'

            ItemLabel:
                id: p_cont_exit
                text: '0'

            ItemLabel:
                id: delta_t
                text: '0'

            ItemLabel:
                id: time_exit
                text: '0'

            ItemLabel:
                id: total_time
                text: '0'

            ItemLabel:
                id: return_time
                text: '0'


    BoxLayout:
        size_hint: 0.9, 0.15
        padding: [30, 0, 30, 20]

        Button:
            text: 'РАСЧЁТ'
            font_size: '40sp'
            # Создаём обработчик кнопки
            on_release:
                root.calculate()

'''
root = Builder.load_string(KV)



def get_values(p_min):
    p_max_drop = str(math.ceil(float(p_min) / 3))

    p_cont_exit = str(int(p_min) - int(p_max_drop))

    delta_t = str(int((int(p_max_drop) * 6.8 / 45)))

    total_time = str(int(int(p_min) * 6.8 / 45))

    return {'p_max_drop': p_max_drop, 'p_cont_exit': p_cont_exit,
            'delta_t': delta_t, 'total_time': total_time}



class Container(GridLayout):

    def calculate(self):
        try:
            pressure = int(self.text_input.text)
        except:
            pressure = 0

        values = get_values(pressure)

        self.p_max_drop.text = values.get('p_max_drop')
        self.p_cont_exit.text = values.get('p_cont_exit')
        self.delta_t.text = values.get('delta_t')
        self.time_exit.text = values.get('delta_t')
        self.total_time.text = values.get('total_time')
        self.return_time.text = values.get('total_time')



class MyApp(App):
    title = 'ZhV'
    def build(self):
        return Container()

if __name__ == "__main__":
    MyApp().run()
