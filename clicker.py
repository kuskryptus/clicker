import pyautogui, sys
import time
import os
from PIL import ImageGrab
import platform



target_color = (0, 122, 255)

initialized = {'join':0, 'confirm':0}
current_dir = os.path.dirname(__file__)
sound_file = os.path.join(current_dir, 'success.mp3')



def play_sound():
    try:
        system_platform = platform.system()
        if system_platform == 'Windows':
            import winsound
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)
        else:
            if sys.platform.startswith('linux'):
                os.system(f"aplay {sound_file} &")
            elif sys.platform.startswith('darwin'):
                os.system(f"afplay {sound_file} &")
    except Exception as e:
        print("Error occurred while playing sound:", e)


def get_clocation(location):
    first_count = 0
    if location == "join" and initialized['join'] == 0:
        try:
            while True:
                x, y = pyautogui.position()
                first_count += 1
                if first_count > 5:
                    initialized['join'] = 1
                    print(initialized)
                    play_sound()
                    first_count = 0
                    return x, y
        except KeyboardInterrupt:
            print('\n')
    elif location == 'confirm' and initialized['confirm'] == 0:
        try:
            while True:
                x, y = pyautogui.position()
                print("position 2", x,y )
                first_count += 1
                if first_count > 5:
                    initialized['confirm'] = 1
                    print(initialized)
                    play_sound()
                    first_count = 0
                    return x, y
        except KeyboardInterrupt:
            print('\n')
     
    return None

time.sleep(5)
x1, y1 = get_clocation('join')
print(x1,y1)
time.sleep(5)
x2, y2 = get_clocation('confirm')

while True:
    print("Start of the loop", x1, y1)
    time.sleep(1)
    pixel_color = ImageGrab.grab().getpixel((x1, y1))
    print(pixel_color)
    if pixel_color == target_color:
        print("Moving to join", x1, y1)
        pyautogui.moveTo(x1, y1)
        pyautogui.click()
        
        time.sleep(1)
     
        pyautogui.moveTo(x2, y2)
        print("Moving to confirm", x2, y2)
        pyautogui.click()

    else:
        break
	
