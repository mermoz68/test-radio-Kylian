input.onButtonPressed(Button.A, function () {
    if (port < 1) {
        basic.showIcon(IconNames.No)
        basic.pause(100)
        basic.clearScreen()
        port = 0
    } else {
        port += 0 - 1
        radio.setGroup(port)
        basic.showNumber(port)
        basic.pause(100)
        basic.clearScreen()
    }
})
function validation () {
    basic.showIcon(IconNames.Yes)
    serial.writeLine("send!")
    basic.pause(100)
    basic.clearScreen()
}
input.onButtonPressed(Button.AB, function () {
    lastport = port
    basic.clearScreen()
    led.plot(0, 2)
    port = 0
    for (let index = 0; index < 256; index++) {
        radio.setGroup(port)
        radio.sendString("!K")
        serial.writeLine("" + port)
        port += 1
        if (port == 85) {
            led.plot(2, 2)
        }
        if (port == 170) {
            led.plot(4, 2)
        }
    }
    radio.setGroup(lastport)
    port = lastport
    validation()
})
radio.onReceivedString(function (receivedString) {
    serial.writeLine(receivedString)
    basic.showString(receivedString)
    basic.pause(2000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (port > 254) {
        basic.showIcon(IconNames.No)
        basic.pause(100)
        basic.clearScreen()
        port = 255
    } else {
        port += 1
        radio.setGroup(port)
        basic.showNumber(port)
        basic.pause(100)
        basic.clearScreen()
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendString("K")
    validation()
})
let lastport = 0
let port = 0
radio.setGroup(port)
