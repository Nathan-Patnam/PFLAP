'''
'''

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color,  Rectangle, Ellipse
from random import random as r
from functools import partial

class DfaScreen(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        self.__canvas = Widget()

        # with self.__canvas.canvas:
        #     self.__canvas.canvas.add(Rectangle(size=(50, 50)))

        #     #self.__canvas.bg_rect = Rectangle( source="cover.jpg", pos=self.pos, size=self.size)
        #     self.__canvas.bind()
        root.add_widget(self.__canvas)

        self.__canvas_nav_bar = NavBar(self.__canvas)
        self.__canvas.bind(on_touch_down=self.onPressed)
        
        root.add_widget(self.__canvas_nav_bar.layout)
        return root
    
    
    
    def redraw(self, args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos


    

    def onPressed(self, a, event):
        current_mode = self.get_current_mode()
        print(current_mode)
        if current_mode == "ADD_STATE":
            self.draw_state(event)
        elif current_mode == "MOVE_STATE":
            print("move state")
        elif current_mode == "ADD_TRANSITION_ARROW":
            print("add transition state")
        elif current_mode == "DELETE_STATE":
            print("delete state")
        elif current_mode == "EDIT_STATE":
            print("edit state")

    
    def draw_state(self, event):
        coordinates = event.pos
        x = coordinates[0]
        y = coordinates[1]
        canvas = self.get_canvas()
        Color(1, 1, 0)
        canvas.add(Color(1., 1., 0))
        canvas.add(Ellipse(pos=(x - 50, y - 50), size=(100, 100)))


    
    def get_canvas(self):
        return self.__canvas.canvas
    
    
    def get_current_mode(self):
        current_mode = self.__canvas_nav_bar.get_current_mode()
        return current_mode
    
class NavBar():
    def __init__(self, wid):
        self.current_mode = "MOVE_STATE"
        self.widget = wid
        self.layout = BoxLayout(size_hint=(1, None), height=50)
        self.draw_move_state_button()
        self.draw_add_state_button()
        self.draw_add_transition_button()
        self.draw_edit_state_button()
        self.draw_delete_state_button()

    

    def draw_move_state_button(self):
        self.add_button("Move state", partial(self.set_current_mode, "MOVE_STATE"))
    
    def draw_add_state_button(self):
        self.add_button("Add state", partial(self.set_current_mode, "ADD_STATE"))


    def draw_add_transition_button(self):
        self.add_button("Add Transition Arrow", partial(
            self.set_current_mode, "ADD_TRANSITION_ARROW"))

    def draw_edit_state_button(self):
        self.add_button("Edit State", partial(
            self.set_current_mode, "EDIT_STATE"))
    
    def draw_delete_state_button(self):
        self.add_button("Delete State", partial(
            self.set_current_mode, "DELETE_STATE"))

    
    def add_button(self, name, on_click_callback):
        button_label = Label(text='0')
        button = Button(text=name,
                        on_press=on_click_callback)
        self.layout.add_widget(button)
    
    def set_current_mode(self, new_mode, c):
        self.current_mode = new_mode
    
    def add_rects(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 1, 1, mode='hsv')
                Rectangle(pos=(r() * wid.width + wid.x,
                                r() * wid.height + wid.y), size=(20, 20))
    
    def get_current_mode(self):
        return self.current_mode

        
if __name__ == '__main__':
    DfaScreen().run()
