let count = 0;
basic.showIcon(IconNames.Heart);

input.onButtonPressed(Button.A, function button_a() {
    count++;

    if (count > 2) {
        count = 0;
    }

    if (count == 0) {
        basic.showIcon(IconNames.Heart);
    } else if (count == 1) {
        basic.showIcon(IconNames.No);
    } else if (count == 2) {
        basic.showIcon(IconNames.Square);
    }

})