#FINISHED - Creating the AttributeSelector class which combinines the label, buttons, and field 
#           for each of the different ball properties.
#         - Cleaning out the UI creation code that was moved to the AttributeSelector class 
#
#TODO     - Implement the AttributeSelector objects.
#         - Figure out a way to create the constant lists from Constants.py that doesn't
#           clutter up the code in this one (defeating the purpose of doing the above).
#         -***NEW IDEA -> Create a GUIInit class to create the lists, and have
#           a function that returns a list of lists (if that is even possible)
#           
#NEXT UP  - Figure out a way to isolate the event handling code into it's own class.
import pygame
import pygame_gui
from Velocity import Velocity
from Ball import Ball
#
# This class creates and handles the GUI for the program
#
class GUI:
    def __init__(self, x, y):
        self.manager = pygame_gui.UIManager((x, y))
        
        #The balls of the program (ha ha ha)
        self.ball_dict = []
        
        

    #
    # check_event does the event handling for the GUI
    #
    def check_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.add_ball_button:
                pass
            if event.ui_element == self.x_pos_up_button:
                num = int(self.x_pos_field.get_text())
                num += 1
                self.x_pos_field.set_text(str(num))
        
            if event.ui_element == self.x_pos_down_button:
                num = int(self.x_pos_field.get_text())
                num -= 1
                self.x_pos_field.set_text(str(num))
        
            if event.ui_element == self.y_pos_up_button:
                num = int(self.y_pos_field.get_text())
                num += 1
                self.y_pos_field.set_text(str(num))
                
            if event.ui_element == self.y_pos_down_button:
                num = int(self.y_pos_field.get_text())
                num -= 1
                self.y_pos_field.set_text(str(num))
                
            if event.ui_element == self.x_vel_up_button:
                num = int(self.x_vel_field.get_text())
                num += 1
                self.x_vel_field.set_text(str(num))
                
            if event.ui_element == self.x_vel_down_button:
                num = int(self.x_vel_field.get_text())
                num -= 1
                self.x_vel_field.set_text(str(num))
                
            if event.ui_element == self.y_vel_up_button:
                num = int(self.y_vel_field.get_text())
                num += 1
                self.y_vel_field.set_text(str(num))
            if event.ui_element == self.y_vel_down_button:
                num = int(self.y_vel_field.get_text())
                num -= 1
                self.y_vel_field.set_text(str(num))
            if event.ui_element == self.energy_level_up_button:
                num = int(self.energy_level_field.get_text())
                num += 1
                self.energy_level_field.set_text(str(num))
            if event.ui_element == self.energy_level_down_button:
                num = int(self.energy_level_field.get_text())
                num -= 1
                self.energy_level_field.set_text(str(num))
            if event.ui_element == self.add_ball_button:
                self.add_ball()
        self.manager.process_events(event)
        
    def update(self, time_delta):
        self.manager.update(time_delta)

        for i in range(0, self.ball_dict.len()):
            self.ball_dict[i].update()

        self.collision_detection()
                            
    def draw(self, window):
        self.manager.draw_ui(window)
        
        for i in range(0, self.ball_dict.len()):
            self.ball_dict[i].draw(window)

    def collision_detection(self):
        for i in self.ball_dict:
            for j in range(i, self.ball_dict.len()):
                self.ball_dict[j].check_collision(self.ball_dict[i])
    #
    #Function executed when user presses "Add Ball" button
    #
    def add_ball(self):
        vel = Velocity(int(self.x_vel_field.get_text()),
                       int(self.y_vel_field.get_text()))
        return_ball = Ball(int(self.x_pos_field.get_text()),
                           int(self.y_pos_field.get_text()),
                           25,
                           int(self.energy_level_field.get_text()),
                           vel,
                           (255,255,255))
        self.ball_dict.append(return_ball)

