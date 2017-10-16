#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U
import ui

def answer_button_touch_up_inside(sender):
    view['area_answer'].text = 'Area = ' + str(3*5) + ' cm^2'
    view['perimeter_answer'].text = 'Perimeter = ' + str(2*(5+3)) + ' cm'
    
view = ui.load_view()
view.present('full_screen')
