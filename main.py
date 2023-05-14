def on_button_pressed_a():
    global port
    if port < 1:
        basic.show_icon(IconNames.NO)
        basic.pause(100)
        basic.clear_screen()
        port = 0
    else:
        port -= 1
        radio.set_group(port)
        basic.show_number(port)
        basic.pause(100)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def validation():
    basic.show_icon(IconNames.YES)
    serial.write_line("send!")
    basic.pause(100)
    basic.clear_screen()

def on_button_pressed_ab():
    global lastport, port
    lastport = port
    basic.clear_screen()
    led.plot(0, 2)
    port = 0
    for index in range(256):
        radio.set_group(port)
        radio.send_string("!K")
        serial.write_line("" + str((port)))
        port += 1
        if port == 85:
            led.plot(2, 2)
        if port == 170:
            led.plot(4, 2)
    radio.set_group(lastport)
    port = lastport
    validation()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    serial.write_line(receivedString)
    basic.show_string(receivedString)
    basic.pause(2000)
    basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global port
    if port > 254:
        basic.show_icon(IconNames.NO)
        basic.pause(100)
        basic.clear_screen()
        port = 255
    else:
        port += 1
        radio.set_group(port)
        basic.show_number(port)
        basic.pause(100)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.send_string("K")
    validation()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

lastport = 0
port = 0
radio.set_group(port)