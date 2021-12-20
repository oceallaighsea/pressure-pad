input.onPinPressed(TouchPin.P0, function () {
    serial.writeLine("0")
    basic.showLeds(`
        . # # # .
        . # . # .
        . # . # .
        . # . # .
        . # # # .
        `)
    basic.pause(5000)
})
function dotDot () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        `)
}
input.onPinPressed(TouchPin.P2, function () {
    serial.writeLine("2")
    basic.showLeds(`
        . # # # .
        . . . # .
        . # # # .
        . # . . .
        . # # # .
        `)
})
input.onPinPressed(TouchPin.P1, function () {
    serial.writeLine("1")
    basic.showLeds(`
        . # # . .
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        `)
})
basic.showIcon(IconNames.Diamond)
serial.redirect(
SerialPin.P0,
SerialPin.P1,
BaudRate.BaudRate115200
)
serial.redirectToUSB()
basic.forever(function () {
    dotDot()
})
