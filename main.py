def WTF():
    global temp
    strip.set_brightness(20)
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P1, True, False, True)
    dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
    basic.pause(1000)
    temp = dht11_dht22.read_data(dataType.TEMPERATURE)
    ESP8266ThingSpeak.connect_thing_speak("api.thingspeak.com",
        "F3CH19DDYVTDD19C",
        temp,
        2,
        0,
        0,
        0,
        0,
        0,
        0)
    basic.show_icon(IconNames.CONFUSED)
    if temp <= 20:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
    elif temp > 80 and temp <= 90:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.RED))
    elif temp > 90 and temp <= 100:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.RED))
    elif temp > 40 and temp <= 50:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
    elif temp > 50 and temp <= 60:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.RED))
    elif temp > 60 and temp <= 70:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.RED))
    elif temp > 70 and temp <= 80:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
        strip.show()
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
    strip.show()
    basic.show_icon(IconNames.TSHIRT)
temp = 0
strip: neopixel.Strip = None
ESP8266ThingSpeak.connect_wifi(SerialPin.P8,
    SerialPin.P12,
    BaudRate.BAUD_RATE115200,
    "DSUconsole",
    "DixieStateConsole")
ESP8266ThingSpeak.wait(5000)
dht11_dht22.select_temp_type(tempType.FAHRENHEIT)
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)
basic.show_icon(IconNames.HEART)

def on_every_interval():
    WTF()
loops.every_interval(30000, on_every_interval)
