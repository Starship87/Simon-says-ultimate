from adafruit_circuitplayground.express import cpx
import time
import random
colors = [(255,0,0), (0,0,255), (0,255,0),(244, 252, 3), (206, 3, 252)]
r =(random.randint(0, len(colors)-1))
s =(random.randint(0, len(colors)-1))
q =(random.randint(0, len(colors)-1))
a =(random.randint(0, len(colors)-1))
color = colors[r]
print (color)
while True:
    if cpx.touch_A1:
        cpx.stop_tone()
    #if cpx.touch_A2:
        #cpx.play_tone(300,1)
        #cpx.play_tone(350,1)
        #cpx.play_tone(400,1)
        #cpx.play_tone(450,1)
        #cpx.play_tone(450,1)
        #cpx.play_tone(400,1)
        #cpx.play_tone(350,1)
        #cpx.play_tone(300,1)
        #cpx.play_tone(250,1)
    if cpx.button_a:
       cpx.pixels [r] = colors[r]
       time.sleep(2)
       cpx.pixels.fill((0, 0,0))
       time.sleep(0.5)
       cpx.pixels [s] = colors[s]
       time.sleep(2)
       cpx.pixels.fill((0, 0,0))
       time.sleep(0.5)
       cpx.pixels [q] = colors[q]
       time.sleep(2)
       cpx.pixels.fill((0, 0,0))
       time.sleep(0.5)
       cpx.pixels [a] = colors[a]
       time.sleep(2)
       cpx.pixels.fill((0, 0,0))
       time.sleep(0.5)

       cpx.pixels.brightness = 0.1
       cpx.pixels.show()
    if cpx.button_b:
       cpx.pixels.fill((0, 0,0))
       cpx.pixels.brightness = 0
       cpx.pixels.show()




