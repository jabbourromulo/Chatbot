import sys, os
import subprocess as sp

print("1- Abrir link da Web: ")
menuItem = int(input())
link = input("Digite o link que você gostaria de abrir\n")
#print(type(menuItem))

def AbreLink(web):
    platform = sys.platform

    if ("win" in platform):
        os.startfile(f"{web}")
    elif ("linux" in platform):
        try:
            sp.Popen(f"{web}")
        except FileNotFoundError:
            sp.Popen(["xdg-open", f"{web}"])

if (menuItem == 1):
    AbreLink(link)
