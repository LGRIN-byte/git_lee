import os
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from tkinter import Tk, BOTH, Menu
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        self.cols=1

       
        self.inside=GridLayout()
        self.inside.cols=1

        self.inside.add_widget(Label(text="도서관 예약 시스템", font_name=fontName, font_size=40, color=(1,2,0,1)))

        

        self.inside.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)
        self.inside.add_widget(Label(text='number'))
       # self.password = TextInput(password=True, multiline=False)
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)
      
          
        self.sumit=Button(text="Sumit",font_size=40)
        #if (self.username.text==): 
        #   if (self.password.text==up):
        #        self.sumit.bind(on_press=self.pressed4)
        #        self.inside.add_widget(self.sumit)
        #        self.add_widget((self.inside))

       # else:
        self.sumit.bind(on_press=self.pressed0)
        self.inside.add_widget(self.sumit)
        self.add_widget((self.inside))

      #  self.add_widget((self.inside))

     #   self.add_widget((self.inside))

    
     
    def pressed4(self,instance):
         
        print("User name:",self.username.text,"Password:",self.password.text)
        self.username.text=""
        self.password.text=""

        
    def pressed0(self,instance):
       # if(self.username==1): 
          # if (self.password.text==1):
        chat_app.screen_manager.current="MainPage"
        
            #    print("User name:",self.username.text,"Password:",self.password.text)
        
#    self.username.text=""
#    self.password.text=""
        


class MainPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        self.cols=1

        self.img=Image(source="logo.jpg")
        self.add_widget(self.img)

        self.inside=GridLayout()
        self.inside.cols=1

        self.inside.add_widget(Label(text="도서관 예약 시스템", font_name=fontName, font_size=40, color=(1,1,1,1)))
        self.inside2 = GridLayout()
        self.inside2.cols = 2

        self.button2_2 = Button(text="이전으로", font_name=fontName,
        font_size=15, color=(1, 1, 1, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_2.bind(on_press=self.pressed2)
        self.inside2.add_widget(self.button2_2)
        self.inside.add_widget(self.inside2)
      
        self.add_widget((self.inside))



        self.button1=Button(text="예약하기\n        (여기를 눌러주세요)",
                            font_name=fontName, font_size=15, color=(1,1,1,1), background_color=(0,0.2,1,1))
      #  background_color=0033FF
        self.button1.bind(on_press=self.pressed)
        self.inside2.add_widget(self.button1)

       

    def pressed(self, instance):
        chat_app.screen_manager.current="InfoPage"

    def pressed2(self, instance):
        chat_app.screen_manager.current="LoginScreen"


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        menu_result= Menu()
        self.cols = 1

        self.img = Image(source="after.jpg")
        self.add_widget(self.img)

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="위치선택\n{}".format(menu_result), font_name=fontName, font_size=15))

        self.inside2 = GridLayout()
        self.inside2.cols = 5

        self.button2_5 = Button(text="로그인화면으로", font_name=fontName,
        font_size=15, color=(1, 1, 1, 1), background_color=(1, 0.2, 1, 1))
        #background_color=FF3300
        self.button2_5.bind(on_press=self.pressed5)
        self.inside2.add_widget(self.button2_5)


        self.button2_1 = Button(text="중앙도서관 열람실", font_name=fontName,
        font_size=15, color=(1, 1, 1, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=66FF33

        self.button2_1.bind(on_press=self.pressed1)
        self.inside2.add_widget(self.button2_1)
       # self.inside.add_widget(self.inside2)
    

        self.button2_2 = Button(text="중앙도서관 레퍼런스", font_name=fontName,
        font_size=15, color=(1, 1, 1, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=FF3300
        self.button2_2.bind(on_press=self.pressed2)
        self.inside2.add_widget(self.button2_2)
       

        self.button2_3 = Button(text="미래", font_name=fontName,
        font_size=15, color=(1, 1, 1, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=FF3300
        self.button2_3.bind(on_press=self.pressed3)
        self.inside2.add_widget(self.button2_3)
       
        self.button2_4 = Button(text="열람실", font_name=fontName,
        font_size=15, color=(1, 1, 1, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=FF3300
        self.button2_4.bind(on_press=self.pressed4)
        self.inside2.add_widget(self.button2_4)

        self.inside.add_widget(self.inside2)


        self.add_widget((self.inside))

    def do_action(self):
        self.menu_result= Menu()



    def pressed1(self, instance):
        chat_app.screen_manager.current = "InfoPage2"

    def pressed2(self, instance):
        chat_app.screen_manager.current = "InfoPage3"

    def pressed3(self, instance):
        chat_app.screen_manager.current = "InfoPage4"

    def pressed4(self, instance):
        chat_app.screen_manager.current = "InfoPage5"

    def pressed5(self, instance):
        chat_app.screen_manager.current="LoginScreen"

class InfoPage1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        menu_result= Menu()
        self.cols = 1

        self.img = Image(source="logo.jpg")
        self.add_widget(self.img)

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="위치선택\n", font_name=fontName, font_size=15))

        self.inside2 = GridLayout()
        self.inside2.cols = 4

        self.button2_1 = Button(text="중앙도서관 열람실", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=66FF33
        self.button2_1.bind(on_press=self.pressed1)
        self.inside2.add_widget(self.button2_1)
       # self.inside.add_widget(self.inside2)
    

        self.button2_2 = Button(text="중앙도서관 레퍼런스", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_2.bind(on_press=self.pressed2)
        self.inside2.add_widget(self.button2_2)
       

        self.button2_3 = Button(text="미래혁신관", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_3.bind(on_press=self.pressed3)
        self.inside2.add_widget(self.button2_3)
       
        self.button2_4 = Button(text="열람실", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_4.bind(on_press=self.pressed4)
        self.inside2.add_widget(self.button2_4)
        self.inside.add_widget(self.inside2)

        self.add_widget((self.inside))

    def do_action(self):
        self.menu_result= Menu()


    def pressed1(self, instance):
        chat_app.screen_manager.current="EndPage"

    def pressed2(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed3(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed4(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed1(self, instance):
        chat_app.screen_manager.current = "InfoPage2"

    def pressed2(self, instance):
        chat_app.screen_manager.current = "InfoPage3"

    def pressed3(self, instance):
        chat_app.screen_manager.current = "InfoPage4"

    def pressed4(self, instance):
        chat_app.screen_manager.current = "InfoPage5"

    def pressed5(self, instance):
        chat_app.screen_manager.current="LoginScreen"


class InfoPage2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        menu_result= Menu()
        self.cols = 1

        self.img = Image(source="after.jpg")
        self.add_widget(self.img)

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="자리 선택", font_name=fontName, font_size=15))

        self.inside2 = GridLayout()
        self.inside2.cols = 4

        self.button2_1 = Button(text="중앙도서관 열람실", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=66FF33
        self.button2_1.bind(on_press=self.pressed1)
        self.inside2.add_widget(self.button2_1)
       # self.inside.add_widget(self.inside2)
    

        self.button2_2 = Button(text="중앙도서관 레퍼런스", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_2.bind(on_press=self.pressed2)
        self.inside2.add_widget(self.button2_2)
       

        self.add_widget((self.inside))

    def do_action(self):
        self.menu_result= Menu()


    def pressed1(self, instance):
        chat_app.screen_manager.current="LoginPage"

    def pressed2(self, instance):
        chat_app.screen_manager.current = "InfoPage3"


class InfoPage3(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        menu_result= Menu()
        self.cols = 1

        self.img = Image(source="after.jpg")
        self.add_widget(self.img)

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="위치선택\n{}".format(menu_result), font_name=fontName, font_size=15))

        self.inside2 = GridLayout()
        self.inside2.cols = 4

        self.button2_1 = Button(text="중앙도서관 열람실", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=66FF33
        self.button2_1.bind(on_press=self.pressed1)
        self.inside2.add_widget(self.button2_1)
       # self.inside.add_widget(self.inside2)
    

        self.button2_2 = Button(text="중앙도서관 레퍼런스", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_2.bind(on_press=self.pressed2)
        self.inside2.add_widget(self.button2_2)
       

        self.button2_3 = Button(text="미래", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_3.bind(on_press=self.pressed3)
        self.inside2.add_widget(self.button2_3)
       
        self.button2_4 = Button(text="열람", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_4.bind(on_press=self.pressed4)
        self.inside2.add_widget(self.button2_4)
        self.inside.add_widget(self.inside2)

        self.add_widget((self.inside))

    def do_action(self):
        self.menu_result= Menu()


    def pressed1(self, instance):
        chat_app.screen_manager.current="EndPage"

    def pressed2(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed3(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed4(self, instance):
        chat_app.screen_manager.current = "Mainpage"


class InfoPage4(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        menu_result= Menu()
        self.cols = 1

        self.img = Image(source="after.jpg")
        self.add_widget(self.img)

        self.inside = GridLayout()
        self.inside.cols = 1

        self.inside.add_widget(Label(text="위치선택\n{}".format(menu_result), font_name=fontName, font_size=15))

        self.inside2 = GridLayout()
        self.inside2.cols = 4

        self.button2_1 = Button(text="중앙도서관 열람실", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(0.4, 1, 0.2, 1))
        #background_color=66FF33
        self.button2_1.bind(on_press=self.pressed1)
        self.inside2.add_widget(self.button2_1)
       # self.inside.add_widget(self.inside2)
    

        self.button2_2 = Button(text="중앙도서관 레퍼런스", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_2.bind(on_press=self.pressed2)
        self.inside2.add_widget(self.button2_2)
       

        self.button2_3 = Button(text="미래", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_3.bind(on_press=self.pressed3)
        self.inside2.add_widget(self.button2_3)
       
        self.button2_4 = Button(text="열람", font_name=fontName,
        font_size=15, color=(0, 0, 0, 1), background_color=(1, 0.2, 0, 1))
        #background_color=FF3300
        self.button2_4.bind(on_press=self.pressed4)
        self.inside2.add_widget(self.button2_4)
        self.inside.add_widget(self.inside2)

        self.add_widget((self.inside))

    def do_action(self):
        self.menu_result= Menu()


    def pressed1(self, instance):
        chat_app.screen_manager.current="EndPage"

    def pressed2(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed3(self, instance):
        chat_app.screen_manager.current = "Mainpage"

    def pressed4(self, instance):
        chat_app.screen_manager.current = "Mainpage"

class EndPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fontName = '/'.join([os.getenv('SystemRoot'), '/fonts/gulim.ttc'])
        self.cols=1

        self.img=Image(source="logo.jpg")
        self.add_widget(self.img)

        self.inside=GridLayout()
        self.inside.cols=1

        self.inside.add_widget(Label(text="나가기", font_name=fontName, font_size=15, color=(1,0,0,1)))

        self.inside.add_widget(Label(text="처음으로 돌아가기", font_name=fontName, font_size=15, color=(1, 0, 0, 1)))
        ##############################################################

        self.add_widget((self.inside))



class EpicApp(App):
    def build(self):
        self.screen_manager= ScreenManager()


        self.connect_page=LoginScreen()
        screen=Screen(name="LoginScreen")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)


        self.connect_page=MainPage()
        screen=Screen(name="MainPage")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page=InfoPage()
        screen = Screen(name="InfoPage")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        self.info_page1=InfoPage1()
        screen = Screen(name="InfoPage1")
        screen.add_widget(self.info_page1)
        self.screen_manager.add_widget(screen)

        self.info_page2=InfoPage2()
        screen = Screen(name="InfoPage2")
        screen.add_widget(self.info_page2)
        self.screen_manager.add_widget(screen)

        self.info_page3=InfoPage3()
        screen = Screen(name="InfoPage3")
        screen.add_widget(self.info_page3)
        self.screen_manager.add_widget(screen)

        self.info_page4=InfoPage4()
        screen = Screen(name="InfoPage4")
        screen.add_widget(self.info_page4)
        self.screen_manager.add_widget(screen)

        self.end_page=EndPage()
        screen = Screen(name="EndPage")
        screen.add_widget(self.end_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager



if __name__ == "__main__":
    chat_app=EpicApp()
    chat_app.run()
    
