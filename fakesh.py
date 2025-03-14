from os import system as execmd
hn = input("cfg:") #.rstrip()
crSh = input("sh_choice:") #.rstrip()

#zsh: command not found: ajsdf
while True:
    cin = input(hn).split(' ')[0]
    print(crSh + ": command not found: " + cin)
