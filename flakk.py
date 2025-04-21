# FLAKK - Simple Scanner
# Developed by napalm
# Github: https://github.com/danapalm

import pyfiglet
from InquirerPy import inquirer
from colorama import Fore, Style, init

from scripts import simple_domains

init(autoreset=True)

# User choice
action = ""

# Info template by napalm (me <3)
def intro():
  f = pyfiglet.Figlet(font="larry3d")
  print(Fore.CYAN + Style.BRIGHT + f.renderText("FLAKK"))
  print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "FLAKK - Custom web scanner version 0.3.6")
  print(Fore.LIGHTBLACK_EX + "Developed by napalm (danapalm) ❤️")
  print(Fore.LIGHTBLACK_EX + "Github: https://github.com/danapalm")

# Main menu
def dynamic_menu():
    while True:
      simple_domains.is_online('http://www.google.com',3)
      action = inquirer.select(
          message="There is:",
          choices=[
              "Scann domain",
              "Exit"
          ],
          default="Scann domain",
      ).execute()

      if "Scann" in action:
          simple_domains.simple_scan_menu()
          intro()
      elif "Exit" in action:
          simple_domains.clear()
          break

# Execute
simple_domains.clear()
intro()
dynamic_menu()
