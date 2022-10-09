def on_received_value(name, value):
    basic.show_string(name)
    basic.show_number(value)
radio.on_received_value(on_received_value)

def on_forever():
    radio.set_group(1)
    basic.pause(30000)
    radio.set_group(2)
    basic.pause(30000)
basic.forever(on_forever)
