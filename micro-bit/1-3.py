count = 0
basic.show_icon(IconNames.HEART)

def button_a():
    global count
    count+=1

    if count > 2:
        count = 0

    if count == 0:
        basic.show_icon(IconNames.HEART)
    elif count == 1:
        basic.show_icon(IconNames.NO)
    elif count == 2:
        basic.show_icon(IconNames.SQUARE)

input.on_button_pressed(Button.A, button_a)