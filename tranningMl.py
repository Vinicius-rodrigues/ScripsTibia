import pyautogui as auto
import time

def moveMouse(inicial, final):
    auto.moveTo(inicial, final)


def pressKeyboard(button):
     auto.press(str(button))


contKeybord = 1000

for c in range(contKeybord):

    time.sleep(3)
    moveMouse(0,500)
    pressKeyboard('f12')
    print( "runoouuu")
    time.sleep(3)
    pressKeyboard('f11')
    print( "comeu food")
    time.sleep(47)
    
    moveMouse(500,0)
    moveMouse(0,500)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    auto.press('down')
    time.sleep(10)

    print(c)




