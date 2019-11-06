from adafruit_circuitplayground.express import cpx
import time
import random
colors = [(255,0,0), (0,0,255), (0,255,0),(244, 252, 3), (206, 3, 252)]
r =(random.randint(0, len(colors)-1))

while True:
    if cpx.touch_A1:
        cpx.stop_tone()
    if cpx.touch_A2:
        cpx.play_tone(250,1)
        cpx.play_tone(300,1)
        cpx.play_tone(350,1)
        cpx.play_tone(400,1)
        cpx.play_tone(450,1)
        cpx.play_tone(450,1)
        cpx.play_tone(400,1)
        cpx.play_tone(350,1)
        cpx.play_tone(300,1)
        cpx.play_tone(250,1)
    if cpx.touch_A3:
       cpx.pixels [0] = colors[0]
       cpx.pixels [9] = colors[0]
       cpx.pixels.brightness = 0.1
       cpx.pixels.show()
    if cpx.touch_A4:
       cpx.pixels [1] = colors[1]
       cpx.pixels [8] = colors[1]
       cpx.pixels.brightness = 0.1
       cpx.pixels.show()
    if cpx.touch_A5:
       cpx.pixels [2] = colors[2]
       cpx.pixels [7] = colors[2]
       cpx.pixels.brightness = 0.1
       cpx.pixels.show()
    if cpx.touch_A6:
       cpx.pixels [3] = colors[3]
       cpx.pixels [6] = colors[3]
       cpx.pixels.brightness = 0.1
       cpx.pixels.show()
    if cpx.touch_A7:
       cpx.pixels [4] = colors[4]
       cpx.pixels [5] = colors[4]
       cpx.pixels.brightness = 0.1
       cpx.pixels.show()
    if cpx.button_b:
       cpx.pixels.fill((0, 0,0))
       cpx.pixels.brightness = 0
       cpx.pixels.show()





