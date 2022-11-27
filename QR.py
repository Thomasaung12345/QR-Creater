# pip install pyqrcode
# pip install pypng
# pip install rich
# pip install pystyle

import pyqrcode 
import png
from rich import print
from pyqrcode import QRCode
from pystyle import Box

print(Box.DoubleCube("Welcome From QR code maker."))
print(Box.DoubleCube("Coded By ThomasAung#5599 on Discord"))

print("[cyan]Insert name for QRCode..[cyan]\n")
name = input('>')

print(" ")
print(" ")
print("[cyan]Address(link) of the webpage..[/cyan]\n")
link = input('>')

print(" ")
print(" ")
print("[cyan]Choose Resolution between [/cyan][red]1-20[/red]\n")
res = input('>')

# String which represents the QR code
s = link

# Generate QR code 
url = pyqrcode.create(s)

# Create and save the png file naming QR.png 
url.png(f'{name}.png', scale = res)

print("[#34c73e]Success![/#34c73e]\n")

# Success = Completed making QR code for you !!!

# Coded by ThomasAung#5599 on discord