import pyautogui
import time
import keyboard

print("Coloque no navegador. Pressione ESC para parar o codigo.")
time.sleep(3)

while True:
    if keyboard.is_pressed('Esc'):
        print("Loop encerrado pelo usuário.")
        break

    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(2)
