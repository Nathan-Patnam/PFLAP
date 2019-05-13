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
        self.create_bottom_nav_bars()
        root = BoxLayout(orientation='vertical')
        root.add_widget(self.wid)
        root.add_widget(self.layout)
        return root
    
    def create_bottom_nav_bars(self):
        self.layout = BoxLayout(size_hint=(1, None), height=50)
        self.draw_move_state_button()
        self.draw_add_state_button()
        self.draw_add_transition_button()
        self.draw_edit_state_button()
        self.draw_delete_state_button()
    
    def draw_move_state_button(self):
        self.add_button("Move state", self.add_rects)
    
    def draw_add_state_button(self):
        self.add_button("Add state", self.add_rects)

    def draw_add_transition_button(self):
        self.add_button("Add Transition Arrow", self.add_rects)
    
    def draw_edit_state_button(self):
        self.add_button("Edit State", self.add_rects)
    
    def draw_delete_state_button(self):
        self.add_button("Delete State", self.add_rects)
    
    def add_button(self, name, on_click_callback):
        button_label = Label(text='0')
        button = Button(text=name,
                        on_press=partial(on_click_callback, button_label, self.wid, 100))
        self.layout.add_widget(button)

        
if __name__ == '__main__':
    DfaScreen().run()
