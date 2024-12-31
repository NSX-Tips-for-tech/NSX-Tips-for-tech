from colorama import Fore

# The system Message Tag
SystemTag = "[+]"
C = Fore.YELLOW
C2 = Fore.RED
C3 = Fore.WHITE

# Print the prompt for username
print(C + SystemTag, C3 + "Please enter a username")

# Insert Username
Username = input(C + SystemTag + " " + C3 + "Username: ")

# Print the greeting
print(C + SystemTag, C3 + "Hello", C2 + Username)
