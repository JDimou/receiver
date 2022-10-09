radio.onReceivedValue(function (name, value) {
    basic.showString(name)
    basic.showNumber(value)
})
basic.forever(function () {
    radio.setGroup(1)
    basic.pause(30000)
    radio.setGroup(2)
    basic.pause(30000)
})
