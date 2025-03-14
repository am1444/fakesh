hn = input("cfg:") # prompt for the... prompt??? help my comments pls
crSh = input("sh_choice:") # prompt for shell to mimic

from os import name,system
if name=='posix': # clear screen
    system('clear')
else:
    system('cls')

while True:
    cin = input(hn).split(' ')[0] # user input and get command requested
    print(crSh + ": command not found: " + cin) # print fake error message lol
