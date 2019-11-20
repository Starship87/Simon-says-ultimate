from adafruit_circuitplayground.express import cpx
import time
import random
colors = [(100,0,0), (0,0,100), (0,100,0),(255, 165, 0), (106, 3, 152)]
#red is 0
#blue is 1
#green is 2
#yellow is 3
#purple is 4
r =(random.randint(0, len(colors)-1))
s =(random.randint(0, len(colors)-1))
q =(random.randint(0, len(colors)-1))
a =(random.randint(0, len(colors)-1))
pattern = []
for i in range(100):
    pattern.append(r)
    r =(random.randint(0, len(colors)-1))
print (pattern)
length = 4
l = length
guessmode = False
def guess(g):
    if g == pattern[0]:
        cpx.play_tone(300,1)


def showcolor():
    for i in range(length):
        n = pattern[i]
        cpx.pixels[n] = colors[n]
        cpx.pixels.brightness = 0.05
        time.sleep(1)
        cpx.pixels.fill((0,0,0))
        cpx.pixels.show()

while True:
    if cpx.touch_A3:
        if guessmode:
            guess(0)
    if cpx.touch_A4:
        if guessmode:
            guess(1)
    if cpx.touch_A5:
        if guessmode:
            guess(2)
    if cpx.touch_A6:
        if guessmode:
            guess(3)
    if cpx.touch_A7:
        if guessmode:
            guess(4)

    if cpx.button_a:
        cpx.play_tone(300,1)
        cpx.play_tone(350,1)
        cpx.play_tone(400,1)
        cpx.play_tone(450,1)
        cpx.play_tone(450,1)
        cpx.play_tone(400,1)
        cpx.play_tone(350,1)
        cpx.play_tone(300,1)
        cpx.play_tone(250,1)
        showcolor()
        guessmode = True




