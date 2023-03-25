from Morpion import b1,b2,b3,b4,b5,b6,b7,b8,b9
import pyautogui

#def variables click
cb1=pyautogui.leftClick(b1)
cb2=pyautogui.leftClick(b2)
cb3=pyautogui.leftClick(b3)
cb4=pyautogui.leftClick(b4)
cb5=pyautogui.leftClick(b5)
cb6=pyautogui.leftClick(b6)
cb7=pyautogui.leftClick(b7)
cb8=pyautogui.leftClick(b8)
cb9=pyautogui.leftClick(b9)

def random():
    empty_cells = []
    if b1["text"] == ' ':
        empty_cells.append(cb1)
    if b2["text"] == ' ':
        empty_cells.append(cb2)    
    if b3["text"] == ' ':
        empty_cells.append(cb3)
    if b4["text"] == ' ':
        empty_cells.append(cb4)
    if b5["text"] == ' ':
        empty_cells.append(cb5)
    if b6["text"] == ' ':
        empty_cells.append(cb6)
    if b7["text"] == ' ':
        empty_cells.append(cb7)
    if b8["text"] == ' ':
        empty_cells.append(cb8)
    if b9["text"] == ' ':
        empty_cells.append(cb9)        
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return False