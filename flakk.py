import os
import pyfiglet
from InquirerPy import inquirer
from colorama import Fore, Back, Style, init

from scripts import simple_domains

init(autoreset=True)

action = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
  f = pyfiglet.Figlet(font="larry3d")
  print(Fore.CYAN + Style.BRIGHT + f.renderText("FLAKK"))
  print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "FLAKK - Custom web scanner version 0.3.1.")
  print(Fore.LIGHTBLACK_EX + "Developed by Juan Pablo (danapalm)")
  print(Fore.LIGHTBLACK_EX + "Github: https://github.com/danapalm")

def dynamic_menu():
    while True:
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
          print("Saliendo del programa...")
          clear()
          break

clear()
intro()
dynamic_menu()
