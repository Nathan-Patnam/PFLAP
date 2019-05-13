'''
Canvas stress
=============

This example tests the performance of our Graphics engine by drawing large
numbers of small squares. You should see a black canvas with buttons and a
label at the bottom. Pressing the buttons adds small colored squares to the
canvas.

'''

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial


class DfaScreen(App):

    def add_rects(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 1, 1, mode='hsv')
                Rectangle(pos=(r() * wid.width + wid.x,
                               r() * wid.height + wid.y), size=(20, 20))

    def double_rects(self, label, wid, *largs):
        count = int(label.text)
        self.add_rects(label, wid, count, *largs)

    def reset_rects(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        self.wid = Widget()
        label = Label(text='0')

        self.layout = BoxLayout(size_hint=(1, None), height=50)
        self.draw_move_state_button()
        self.draw_add_state_button()
        self.draw_add_transition_button()
        self.draw_edit_state_button()
        self.draw_delete_state_button()



        #elf.layout.add_widget(btn_double)
        #self.layout.add_widget(btn_reset)

        #self.layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(self.wid)
        root.add_widget(self.layout)

        return root
    
    def draw_move_state_button(self):
        label = Label(text='0')
        btn_add100 = Button(text='Move State',
                            on_press=partial(self.add_rects, label, self.wid, 100))
        self.layout.add_widget(btn_add100)
        
    
    def draw_add_state_button(self):
        label = Label(text='0')
        btn_add100 = Button(text='Add State',
                            on_press=partial(self.add_rects, label, self.wid, 100))
        self.layout.add_widget(btn_add100)
    
    def draw_add_transition_button(self):
        label = Label(text='0')
        btn_add100 = Button(text='Add Transition Arrow',
                            on_press=partial(self.add_rects, label, self.wid, 100))
        self.layout.add_widget(btn_add100)
    
    def draw_edit_state_button(self):
        label = Label(text='0')
        btn_add100 = Button(text='Edit State',
                            on_press=partial(self.add_rects, label, self.wid, 100))
        self.layout.add_widget(btn_add100)
    
    def draw_delete_state_button(self):
        label = Label(text='0')
        btn_add100 = Button(text='Delete State',
                            on_press=partial(self.add_rects, label, self.wid, 100))
        self.layout.add_widget(btn_add100)
        



if __name__ == '__main__':
    DfaScreen().run()
