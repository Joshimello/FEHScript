import pyautogui
import time
import os
from pynput.keyboard import Key, Controller

controller=Controller()

def is_chapter_done():
    timeout = 3
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        exclaim=pyautogui.locateOnScreen('exclaim.png', confidence=.9)
        if exclaim!=None:
            print(">CHAPTER NOT COMPLETE")
            initiate_fight(exclaim)
    print(">CHAPTER COMPLETE")
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('redback.png',  grayscale=True, confidence=.5)))
    timeout = 3
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        exclaim=pyautogui.locateOnScreen('exclaimtwo.png', confidence=.9)
        if exclaim!=None:
            print(">SCROLL")
            pyautogui.click(pyautogui.center(exclaim))
            is_chapter_done()
    
def initiate_fight(exclaim):
    print(exclaim)
    pyautogui.click(pyautogui.center(exclaim))
    time.sleep(1)
    fight=pyautogui.locateOnScreen('fight.png', confidence=.9)
    if fight!=None:
        pyautogui.click(pyautogui.center(fight))
        fight_level()

def fight_level():
    while True:
        auto=pyautogui.locateOnScreen('autofight.png', confidence=.8)
        if auto!=None:
            break
    auto=pyautogui.locateOnScreen('autofight.png', confidence=.8)
    while True:
        time.sleep(0.1)
        pyautogui.click(pyautogui.center(auto))
        autobattle=pyautogui.locateOnScreen('autofightconf.png', confidence=.8)
        if autobattle!=None:
            break
    autobattleconf=pyautogui.locateOnScreen('autofightconf.png', confidence=.8)
    while True:
        pyautogui.click(pyautogui.center(autobattleconf))
        time.sleep(0.1)
        ok=pyautogui.locateOnScreen('ok.png', confidence=.8)
        close=pyautogui.locateOnScreen('close.png', confidence=.8)
        if ok or close!=None:
            claim_reward()
            break

def claim_reward():
    while True:
        ok=pyautogui.locateOnScreen('ok.png', confidence=.8)
        close=pyautogui.locateOnScreen('close.png', confidence=.8)
        if ok or close!=None:
            if ok!=None:
                pyautogui.click(pyautogui.center(ok))
                time.sleep(1)
                back=pyautogui.locateOnScreen('redback.png', confidence=.8)
                if back!=None:
                    break
            if close!=None:
                pyautogui.click(pyautogui.center(close))
                time.sleep(1)
                back=pyautogui.locateOnScreen('redback.png', confidence=.8)
                if back!=None:
                    break
    time.sleep(1)
    is_chapter_done()
        
is_chapter_done()
