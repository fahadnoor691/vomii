import platform
import subprocess
import pyautogui
import os
from datetime import datetime


class DextopAgent:
    def __init__(self):
        self.system = platform.system()

    def open_application(self, app_name):
        try:
            if self.system == "Windows":
                available_apps = {
                    "chrome": "chrome.exe",
                    "notepad": "notepad.exe",
                    "calculator": "calc.exe",
                    "explorer": "explorer.exe",
                    "spotify": "spotify.exe",
                    "powershell": "powershell.exe",
                }

                app_name_lower = app_name.lower()
                actual_app_name = available_apps.get(app_name_lower)

                if actual_app_name:
                    subprocess.Popen(actual_app_name)
                    return f"Opening {app_name}"
                else:
                    return f"{app_name} not found in available applications"
                
            elif self.system == "Linux":
                subprocess.Popen(app_name)
                return f"Opening {app_name}"
            
            elif self.system == "Darwin":
                subprocess.Popen(app_name)
                return f"Opening {app_name}"

        except Exception as e:
            return f"Error: {str(e)}"

    def take_screenshot(self):
        try:
            screenshot = pyautogui.screenshot()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")

            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            save_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
            screenshot.save(save_path)

            if self.system == "Windows":
                os.startfile(save_path)
            elif self.system == "Linux":
                subprocess.run(["xdg-open", save_path])
            elif self.system == "Darwin":
                subprocess.run(["open", save_path])

            return f"Screenshot taken and saved in screenshots folder"
        except Exception as e:
            return f"Error: {str(e)}"

    def minimize_windows(self):
        try:
            if self.system == "Windows":
                pyautogui.hotkey("win", "d")
            elif self.system == "Linux":
                pyautogui.hotkey("alt", "space", "n")
            elif self.system == "Darwin":
                pyautogui.hotkey("alt", "space", "n")

            return "Window minimized"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def restore_windows(self):
        try:
            if self.system == "Windows":
                pyautogui.hotkey("win", "shift", "m")
            elif self.system == "Linux":
                pyautogui.hotkey("alt", "space", "n")
            elif self.system == "Darwin":
                pyautogui.hotkey("alt", "space", "n")

            return "Window restored"
        except Exception as e:
            return f"Error: {str(e)}"


    def close_windows(self):
        try:
            if self.system == "Windows":
                pyautogui.hotkey("alt", "f4")
            elif self.system == "Linux":
                pyautogui.hotkey("alt", "f4")
            elif self.system == "Darwin":
                pyautogui.hotkey("alt", "f4")

            return "Window closed"
        except Exception as e:
            return f"Error: {str(e)}"
        
            
