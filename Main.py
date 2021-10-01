import sys, os
import subprocess as sp

print("1- Abrir link da Web: ")
menuItem = int(input())
#print(type(menuItem))

def AbreLink():
    platform = sys.platform

    if ("win" in platform):
        os.startfile("www.cnbc.com")
    elif ("linux" in platform):
        try:
            sp.Popen("www.cnbc.com")
        except FileNotFoundError:
            sp.Popen(["xdg-open", "www.cnbc.com"])

if (menuItem == 1):
    AbreLink()
