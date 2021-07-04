def shook():
    basic.show_icon(IconNames.NO)

def button_pushed():
    basic.clear_screen()

input.on_gesture(Gesture.SHAKE, shook)
input.on_button_pressed(Button.A, button_pushed)
input.on_button_pressed(Button.B, button_pushed)