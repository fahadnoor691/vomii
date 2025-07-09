import platform
import subprocess
import pyautogui
import os
import ctypes
import psutil
import socket
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

                subprocess.Popen(actual_app_name)
                return f"Opening {app_name}"

            elif self.system == "Linux":
                app_mapping = {
                    "chrome": "google-chrome",
                    "firefox": "firefox",
                    "terminal": "gnome-terminal",
                    "calculator": "gnome-calculator",
                    "files": "nautilus",
                    "gedit": "gedit"
                }
                
                app_name_lower = app_name.lower()
                actual_app_name = app_mapping.get(app_name_lower, app_name)
                
                subprocess.Popen([actual_app_name])
                return f"Opened {actual_app_name}"
            
            if self.system == "Darwin":
                app_mapping = {
                    "chrome": "Google Chrome",
                    "safari": "Safari",
                    "spotify": "Spotify",
                    "terminal": "Terminal",
                    "mail": "Mail",
                    "messages": "Messages",
                    "calculator": "Calculator",
                    "notes": "Notes",
                    "calendar": "Calendar",
                    "maps": "Maps",
                    "weather": "Weather",
                    "clock": "Clock",
                    "settings": "System Preferences",
                    "preferences": "System Preferences"
                }
                
                app_name_lower = app_name.lower()
                actual_app_name = app_mapping.get(app_name_lower, app_name)
                
                subprocess.run(["open", "-a", actual_app_name])
                return f"Opened {actual_app_name}"

        except Exception as e:
            return f"Cannot open {app_name}"

    def take_screenshot(self, filename=None):
        try:
            screenshot = pyautogui.screenshot()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            screenshot_dir = os.getcwd()

            filename = f"{filename}.png" if filename else f"screenshot_{timestamp}.png"

            save_path = os.path.join(screenshot_dir, filename)
            screenshot.save(save_path)

            if self.system == "Windows":
                os.startfile(save_path)
            elif self.system == "Linux":
                subprocess.run(["xdg-open", save_path])
            elif self.system == "Darwin":
                subprocess.run(["open", save_path])

            return f"Screenshot taken and saved as {filename}"
        except Exception as e:
            return f"Could not take screenshot: {str(e)}"

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
            return f"Could not minimize window: {str(e)}"
    
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
            return f"Could not restore window: {str(e)}"

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
            return f"Could not close window: {str(e)}"
    
    def lock_computer(self):
        try:
            if self.system == "Windows":
                ctypes.windll.user32.LockWorkStation()
            elif self.system == "Linux":
                subprocess.run(["gnome-screensaver-command", "-l"])
            elif self.system == "Darwin":
                subprocess.run(["pmset", "displaysleepnow"])
            return "Computer locked"
        except Exception as e:
            return f"Could not lock computer: {str(e)}"

    def get_system_info(self):
        try:
            info = {
                "OS": platform.system(),
                "OS Version": platform.version(),
                "Node": platform.node(),
                "Processor": platform.processor(),
                "CPU Cores": psutil.cpu_count(logical=False),
                "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
                "Disk Space": f"{round(psutil.disk_usage('/').total / (1024**3), 2)} GB"
            }
            return "\n".join(f"{k}: {v}" for k, v in info.items())
        except Exception as e:
            return f"Could not get system info: {str(e)}"
    
    def get_system_battery(self):
        try:
            battery = psutil.sensors_battery()
            if battery is None:
                return "No battery detected (desktop computer or battery not available)"
            return f"Battery: {battery.percent}%"
        except Exception as e:
            return f"Could not get system battery: {str(e)}"
    
    def get_running_apps(self):
        try:
            running_apps = []
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    running_apps.append(proc.info['name'])
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            unique_apps = list(set(running_apps))[:10]
            return f"Running apps: {', '.join(unique_apps)}"
        except Exception as e:
            return f"Could not get running apps: {str(e)}"
    
    def get_ip_address(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)

            return f"IP Address: {ip_address}"
        except Exception as e:
            return f"Could not get IP address: {str(e)}"