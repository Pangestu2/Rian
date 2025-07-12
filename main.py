# import kivy
# from kivy.app import App
# # widget
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget

# class MyApp(App):
#     def build(self):
#         wdg = Widget()
#         lbl = Label(text='Rian Pangestu', pos=(200, 0))
#         btn = Button(text='2211038')
#         wdg.add_widget(lbl)
#         wdg.add_widget(btn)
#         return wdg

# MyApp().run()

# #widget
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# class myApp(App):
#     def build(self):
#         wdg = Widget()
#         lbl = Label(text='Rian Pangestu',pos=(200,0))
#         btn = Button(text='2211038')
#         wdg.add_widget(lbl)
#         wdg.add_widget(btn)
#         return wdg

# myApp().run()

# #boxlayout
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import boxlayout
# class myApp(App):
#     def build(self):
#         blayout = Boxlayout(orientation='vertical')
#         btn1 = Button(text='btn1',size_hint=(0.5,1),pos_hint{'center_x':0,5})
#         btn2 = Button(text='btn2')
#         btn3 = Button(text='btn3')
#         btn4 = Button(text='btn4')
#         layout.add_widget(btn1)
#         layout.add_widget(btn2)
#         layout.add_widget(btn3)
#         layout.add_widget(btn4)
#         return layout

# myApp().run()

# # anchorlayout
# rom kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.anchorlayout import AnchorLayout

# class MyApp(App):
#     def build(self):
#         a_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        
#         btn = Button(text='wandDinulAgil')
#         btn.size_hint = (0.2, 0.2)
        
#         a_layout.add_widget(btn)
#         return a_layout

# myApp().run()

# #gridLayout
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import Gridlayout
# class myApp(App):
#     def build(self):
#         g_layout = Gridlayout(cols=3)
#           btn1 = Button(text='btn1', size_hint=(0.2, 0.2))
#         btn2 = Button(text='btn2', size_hint=(0.2, 0.2))
#         btn3 = Button(text='btn3', size_hint=(0.2, 0.2))
#         btn4 = Button(text='btn4', size_hint=(0.2, 0.2))

#         g_layout.add_widget(btn1)
#         g_layout.add_widget(btn2)
#         g_layout.add_widget(btn3)
#         g_layout.add_widget(btn4)
#         return g_layout

# myApp().run()

# #stackLayout
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.stacklayout import StackLayout

# class MyApp(App):
#     def build(self):
#         s_layout = StackLayout(orientation='lr-tb')  # left to right, top to bottom

#         btn1 = Button(text='btn1', size_hint=(0.2, 0.2))
#         btn2 = Button(text='btn2', size_hint=(0.2, 0.2))
#         btn3 = Button(text='btn3', size_hint=(0.2, 0.2))
#         btn4 = Button(text='btn4', size_hint=(0.2, 0.2))
#         btn5 = Button(text='btn5', size_hint=(0.5, 0.2))

#         s_layout.add_widget(btn1)
#         s_layout.add_widget(btn2)
#         s_layout.add_widget(btn3)
#         s_layout.add_widget(btn4)
#         s_layout.add_widget(btn5)

#         return s_layout

# myApp().run()

#pagelayout
# Mengimpor kelas App dari modul Kivy yang digunakan sebagai dasar aplikasi
from kivy.app import App

# Mengimpor widget Button untuk membuat tombol di tampilan
from kivy.uix.button import Button

# Mengimpor PageLayout, yaitu layout untuk membagi tampilan menjadi beberapa halaman yang bisa digeser (swipe)
from kivy.uix.pagelayout import PageLayout


# Mendefinisikan kelas MyApp yang merupakan turunan dari App
class MyApp(App):

    
    # Fungsi build akan dijalankan pertama kali saat aplikasi dijalankan
    def build(self):

         # Membuat objek layout utama menggunakan PageLayout
        p_layout = PageLayout()

        
        # Membuat tombol pertama dengan teks "Rian" dan ukuran 20% dari lebar dan tinggi layar
        btn1 = Button(text='Rian', size_hint=(0.2, 0.2))

        # Membuat tombol kedua dengan teks "Pangestu" dan ukuran yang sama
        btn2 = Button(text='Pangestu', size_hint=(0.2, 0.2))

        # Membuat tombol ketiga dengan teks "Ganteng" dan ukuran yang sama
        btn3 = Button(text='Ganteng', size_hint=(0.2, 0.2))

        # Menambahkan tombol pertama ke halaman pertama PageLayout
        p_layout.add_widget(btn1)

        # Menambahkan tombol kedua ke halaman kedua PageLayout
        p_layout.add_widget(btn2)

        # Menambahkan tombol ketiga ke halaman ketiga PageLayout
        p_layout.add_widget(btn3)

        # Mengembalikan layout sebagai tampilan utama aplikasi
        return p_layout

# Membuat instance dari MyApp dan menjalankan aplikasi
MyApp().run()

# #floatlayout
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.scatterlayout import ScatterLayout

# class MyApp(App):
#     def build(self):
#         f_layout = FloatLayout()

#         btn1 = Button(
#             text='btn1',
#             size_hint=(0.2, 0.2),
#             pos_hint={'x': 0.4, 'y': 0.4}
#         )

#         f_layout.add_widget(btn1)
#         return f_layout

# if _name_ == '_main_':

#  MyApp().run()

#  #kivy color
#  from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
# from kivy.core.window import Window
# from kivy.utils import get_color_from_hex

# class MyApp(App):
#     def build(self):
#         f_layout = FloatLayout()

#         # Ubah warna latar belakang window
#         Window.clearcolor = get_color_from_hex('#eeeeee')

#         # Tambahkan tombol dengan ukuran dan posisi tertentu
#         btn1 = Button(
#             text='btn1',
#             size_hint=(0.2, 0.2),
#             pos_hint={'x': 0.4, 'y': 0.4}
#         )

#         # Ubah warna latar belakang tombol
#         btn1.background_color = get_color_from_hex('#aaaaaa')

#         f_layout.add_widget(btn1)
#         return f_layout

#  MyApp().run()