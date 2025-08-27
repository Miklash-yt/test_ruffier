from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
from seconds import *
from kivy.core.window import Window
from runner import *
from sits import *


name1 = ''
age1 = 0
pulse_result = 0
pulse_result2 = 0
pulse_result3 = 0

Window.clearcolor = (0.54,0.54,0.54, 1)

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False    



class InstrScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name=name)
        main_layout = BoxLayout(orientation='vertical')
        layout = BoxLayout()
        layout2 = BoxLayout(size_hint=(1, .1))
        layout3 = BoxLayout(size_hint=(1, .1))
        layout4 = BoxLayout(size_hint=(.3, .4), pos_hint={'right':.65 })
        theory_test = Label(text='[size=16]'+'[b]'+'[color=#76ff3b]'+txt_instruction+'[/size]'+'[/color]'+'[/b]', markup=True)
        username = Label(text='[color=#76ff3b]'+'Введите имя'+'[/color]',markup=True)
        user_age = Label(text='[color=#76ff3b]'+'Введите возраст'+'[/color]', markup=True)
        self.name_input = TextInput()
        self.age_input = TextInput()
        resume_button = Button(text='Начать')
        resume_button.background_color = (0.59, 1, 0.85, 1)
        layout.add_widget(theory_test)
        layout2.add_widget(username)
        layout2.add_widget(self.name_input)
        layout3.add_widget(user_age)
        layout3.add_widget(self.age_input)
        layout4.add_widget(resume_button)
        main_layout.add_widget(layout)
        main_layout.add_widget(layout2)
        main_layout.add_widget(layout3)
        main_layout.add_widget(layout4)
        self.add_widget(main_layout)
        resume_button.on_press = self.next_screen
    def next_screen(self):
        global name1, age1   
        name1 = self.name_input.text
        print(name1)
        age1 = check_int(self.age_input.text)
        if age1 == False or age1 < 7:
            age1 = 0
            self.age_input.text = str(age1)
        else:
            self.manager.current = 'two'


class PulseScr(Screen):
    def __init__(self, name = 'two'):
        super().__init__(name=name)
        self.next_scr = False
        self.lbl_sec = Seconds(15)  
        self.lbl_sec.bind(done = self.sec_finished)
        main_lt = BoxLayout(orientation='vertical')
        lt = BoxLayout()
        lt2 = BoxLayout(size_hint=(1,.1))
        lt3 = BoxLayout(size_hint=(.3,.4), pos_hint={'right':.65 })
        pulse_txt = Label(text='[size=13]'+'[color=#76ff3b]'+txt_test1+'[/color]'+'[/size]', markup=True)
        pulse_result11 = Label(text='[color=#76ff3b]'+'Введите результат:'+'[/color]', markup=True)
        self.pulse_result1 = TextInput()
        self.resume_button2 = Button(text='[color=#76ff3b]'+'Начать'+'[/color]', markup=True)
        self.resume_button2.background_color = (0.59, 1, 0.85, 1)
        lt.add_widget(pulse_txt)
        lt.add_widget(self.lbl_sec)
        lt2.add_widget(pulse_result11)
        lt2.add_widget(self.pulse_result1)
        lt3.add_widget(self.resume_button2)
        main_lt.add_widget(lt)
        main_lt.add_widget(lt2)
        main_lt.add_widget(lt3)
        self.add_widget(main_lt)
        self.resume_button2.on_press = self.next_screen
        self.pulse_result1.set_disabled(True)
    
    def sec_finished(self, *args):
        self.next_scr = True
        self.pulse_result1.set_disabled(False)
        self.resume_button2.set_disabled(False)
        self.resume_button2.text = 'Продолжить'
        self.resume_button2.background_color = (0.59, 1, 0.85, 1)
    def next_screen(self):
        global pulse_result
        if not self.next_scr:
            self.resume_button2.set_disabled(True)
            self.lbl_sec.start()
        else:
            pulse_result = check_int(self.pulse_result1.text)
            if pulse_result == False or pulse_result <=0:
                pulse_result = 0
                self.pulse_result1.text = str(pulse_result)
            else:    
                self.manager.current = 'three'

class SquatScr(Screen):
    def __init__(self, name = 'three'):
        super().__init__(name=name)
        self.next_scr = False
        self.lbl_sits = Sits(30)
        self.run = Runner(total=30, steptime = 1.5, size_hint=(0.4, 1))
        self.run.bind(finisheed=self.run_finished)
        main1_layout = BoxLayout(orientation='vertical')
        layout1 = BoxLayout()
        layout22 = BoxLayout(size_hint=(.3,.4), pos_hint={'right':.65 })
        squat = Label(text='[color=#76ff3b]'+txt_test2+'[/color]', markup=True)
        self.resume_button3 = Button(text='[color=#76ff3b]'+'Начать'+'[/color]', markup=True)
        self.resume_button3.background_color = (0.59, 1, 0.85, 1)
        layout1.add_widget(squat)
        layout22.add_widget(self.resume_button3)
        main1_layout.add_widget(layout1)
        main1_layout.add_widget(layout22)
        main1_layout.add_widget(self.run)
        main1_layout.add_widget(self.lbl_sits)
        self.add_widget(main1_layout)
        self.resume_button3.on_press = self.next_screen
    def run_finished(self, instance, value):
        self.resume_button3.set_disabled(False)
        self.resume_button3.text = 'Продолжить'
        self.next_scr = True
    def next_screen(self):
        if not self.next_scr:
            self.resume_button3.set_disabled(True)
            self.run.start()
            self.run.bind(valuee=self.lbl_sits.next)
        else:    
            self.manager.current = 'four'

class SemifinalScr(Screen):
    def __init__(self, name = 'four'):
        super().__init__(name=name)
        self.next_scr = 1
        self.lbl_sec = Seconds(15)  
        self.lbl_sec.bind(done = self.sec_finished)
        main_layout2 = BoxLayout(orientation='vertical')
        lt1 = BoxLayout()
        layout5 = BoxLayout(size_hint=(1, .1))
        layout6 = BoxLayout(size_hint=(1, .1))
        layout7 = BoxLayout(size_hint=(.3, .4), pos_hint={'right':.65 })
        measure_pulse = Label(text='[color=#76ff3b]'+txt_test3+'[/color]', markup=True)
        result_pulse = Label(text='Результат:')
        result_pulse2 = Label(text='Результат после отдыха:') 
        self.input_pulse = TextInput()
        self.input_pulse2 = TextInput()
        self.resume_button4 = Button(text='[color=#76ff3b]'+'Начать'+'[/color]', markup=True)
        self.resume_button4.background_color = (0.59, 1, 0.85, 1)
        lt1.add_widget(measure_pulse)
        layout5.add_widget(result_pulse)
        layout5.add_widget(self.input_pulse)
        layout6.add_widget(result_pulse2)
        layout6.add_widget(self.input_pulse2)
        layout7.add_widget(self.resume_button4)
        main_layout2.add_widget(lt1)
        main_layout2.add_widget(self.lbl_sec)
        main_layout2.add_widget(layout5)
        main_layout2.add_widget(layout6)
        main_layout2.add_widget(layout7)
        self.add_widget(main_layout2)
        self.resume_button4.on_press = self.next_screen 
        self.input_pulse.set_disabled(True)
        self.input_pulse2.set_disabled(True)
    
    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.next_scr == 1:
                self.next_scr = 2
                self.lbl_sec.restart(30)
                self.input_pulse.set_disabled(False)
            elif self.next_scr == 2:
                self.next_scr = 3
                self.input_pulse2.set_disabled(True)
                self.lbl_sec.restart(15)
            elif self.next_scr == 3:
                self.input_pulse2.set_disabled(False)
                self.resume_button4.set_disabled(False)
                self.resume_button4.text = 'Продолжить'
                self.resume_button4.background_color = (0.59, 1, 0.85, 1)



    def next_screen(self):
        global pulse_result2, pulse_result3
        if self.next_scr == 1:
            self.resume_button4.set_disabled(True)
            self.lbl_sec.start()
        else:
            pulse_result2 = check_int(self.input_pulse.text)
            pulse_result3 = check_int(self.input_pulse2.text)
            if pulse_result2 == False or pulse_result2 <=0:
                pulse_result2 = 0
                self.input_pulse.text = str(pulse_result2)
                if pulse_result3 ==  False or pulse_result3 <=0:
                    pulse_result3 = 0
                    self.input_pulse2.text = str(pulse_result3)
            elif pulse_result3 == False or pulse_result3 <=0:
                pulse_result3 = 0
                self.input_pulse2.text = str(pulse_result3)
            else:
                self.manager.current = 'five'

class FinalScr(Screen):
    def __init__(self, name='five'):
        super().__init__(name=name)
        main_layout3 = BoxLayout(orientation='vertical')   
        self.testruffier_name = Label(text='[color=#76ff3b]'+'Ваше имя:'+name1+'[/color]', markup=True)     
        testruffier = Label(text='[color=#76ff3b]'+'Ваш тест Руфье:'+'[/color]', markup=True)
        self.test_ruffier = Label(text='[color=#76ff3b]'+'Работоспособность сердца:'+'[/color]', markup=True)
        main_layout3.add_widget(self.testruffier_name)
        main_layout3.add_widget(testruffier)
        main_layout3.add_widget(self.test_ruffier)
        self.add_widget(main_layout3)
        self.on_enter = self.nameeee
    def nameeee(self):
        self.testruffier_name.text = 'Ваше имя:'+name1
        result_nameeee = test(pulse_result, pulse_result2, pulse_result3, age1)
        self.test_ruffier.text = result_nameeee
        

class MyApp(App):
    def build(self):
        sm = ScreenManager() 
        sm.add_widget(InstrScr(name = 'main'))
        sm.add_widget(PulseScr(name='two'))
        sm.add_widget(SquatScr(name='three'))
        sm.add_widget(SemifinalScr(name='four'))
        sm.add_widget(FinalScr(name='five'))



        return sm

MyApp().run()
