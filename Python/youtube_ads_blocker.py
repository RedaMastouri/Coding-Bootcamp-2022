#Import the required librairies 
import cv2
import numpy as np
import pyautogui as gui
import time

#reading the templates
template1 = cv2.imread('template1.png', 0)
template2 = cv2.imread('template2.png', 0)
template3 = cv2.imread('template3.png', 0)
template4 = cv2.imread('template4.png', 0)

#Defining the threshold
threshold = 0.7

#Returning an alert with sample text and title 
gui.alert(text ='Keep the mouse pointer on the top left corner of the screen to stop the program', title='Stopping Criteria')

#Detecting the ads
while True:
    time.sleep(1)
    im1 = gui.screenshot()
    im1 = np.asarray(im1.convert(mode = 'L'))
    #results
    res = cv2.matchTemplate(im1, template1, cv2.TM_CCOEFF_NORMED )
    loc = np.where(res >=threshold)
    if loc[0].size !=0:
        gui.click(list(zip(*loc[::-1]))[0])

    res = cv2.matchTemplate(im1, template2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >=threshold)
    if loc[0].size !=0:
        gui.click(list(zip(*loc[::-1]))[0])
    
    res = cv2.matchTemplate(im1, template3, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >=threshold)
    if loc[0].size !=0:
        gui.click(list(zip(*loc[::-1]))[0])

    res = cv2.matchTemplate(im1, template4, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >=threshold)
    if loc[0].size !=0:
        gui.click(list(zip(*loc[::-1]))[0])

    if gui.position() == (0,0):
        gui.alert(text ='Ads Skipper is closed', title='Ads Blocker Closed')
        break
    
