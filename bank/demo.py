import os
import pyautogui
import subprocess
import time

def find_and_right_click(folder_path, target_folder_name):
    subprocess.Popen(f'explorer "{folder_path}"')
    time.sleep(3)  # Adjust this value based on your system's responsiveness

    # List items in the folder
    items = os.listdir(folder_path)

    # Check if the target folder is in the list
    if target_folder_name in items:
        # Get the position of the target folder in the window
        target_folder_position = items.index(target_folder_name)
        chooseFolder = 0
        if target_folder_position == 0 :
            chooseFolder = 300 + 25
        else :
            chooseFolder = 300 + target_folder_position * 25

        pyautogui.moveTo(500, chooseFolder)

if __name__ == "__main__":
    folder_path = r"C:\Users\Aliasger B\1001_ai\1001_ai_python\Core_python\bank\safe_root"
    target_folder_name = "hii"
    find_and_right_click(folder_path, target_folder_name)
