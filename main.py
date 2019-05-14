'''
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
    def build(self):
        self.current_mode = "MOVE STATE"

        root = BoxLayout(orientation='vertical')
        canvas = Widget()
        root.add_widget(canvas)

        canvas_nav_bar = NavBar(canvas)
        canvas.bind(on_touch_down=self.onPressed)
        root.add_widget(canvas_nav_bar.layout)
        return root
    

    def onPressed(self, a, event):
        if self.current_mode == "ADD_STATE":
            print("add state")
        elif self.current_mode == "MOVE_STATE":
            print("move state")
        elif self.current_mode == "ADD_TRANSITION_ARROW":
            print("add transition state")
        elif self.current_mode == "DELETE_STATE":
            print("delete state")
        elif self.current_mode == "EDIT_STATE":
            print("edit state")

    
class NavBar():
    def __init__(self, wid):
        self.widget = wid
        self.layout = BoxLayout(size_hint=(1, None), height=50)
        self.draw_move_state_button()
        self.draw_add_state_button()
        self.draw_add_transition_button()
        self.draw_edit_state_button()
        self.draw_delete_state_button()

    

    def draw_move_state_button(self):
        self.add_button("Move state", self.add_state)

    def draw_add_state_button(self):
        self.add_button("Add state", self.change_to_add_state_mode)

    def change_to_add_state_mode(self):
        self.current_mode = "ADD STATE"



    def add_state(self, label, wid, count, *largs):
        with wid.canvas:
            clicked_coordinates = wid.pos
            x = clicked_coordinates[0]
            y = clicked_coordinates[0]
            RADIUS = 25

    def draw_add_transition_button(self):
        self.add_button("Add Transition Arrow", self.add_rects)

    def draw_edit_state_button(self):
        self.add_button("Edit State", self.add_rects)

    def draw_delete_state_button(self):
        self.add_button("Delete State", self.add_rects)

    def add_button(self, name, on_click_callback):
        button_label = Label(text='0')
        button = Button(text=name,
                        on_press=partial(on_click_callback, button_label, self.widget, 100))
        self.layout.add_widget(button)
    
    def add_rects(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 1, 1, mode='hsv')
                Rectangle(pos=(r() * wid.width + wid.x,
                                r() * wid.height + wid.y), size=(20, 20))

        
if __name__ == '__main__':
    DfaScreen().run()
