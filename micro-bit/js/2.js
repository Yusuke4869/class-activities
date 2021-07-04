input.onGesture(Gesture.Shake, function shook() {
    basic.showIcon(IconNames.No);
})

function button_pushed() {
    basic.clearScreen();
}

input.onButtonPressed(Button.A, button_pushed);
input.onButtonPressed(Button.B, button_pushed);