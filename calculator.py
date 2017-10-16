#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U
#  this does basic math

import ui

def equation1_touch_up_inside(sender):
    view['label1'].text = str(5+2**3)
    
def equation2_touch_up_inside(sender):
    view['label2'].text = str(4/2+5)
    
def equation3_touch_up_inside(sender):
    view['label3'].text = str(3+4*2)
    
def equation4_touch_up_inside(sender):
    view['label4'].text = str(7-3+2)

view = ui.load_view()
view.present('full_screen')
