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
print("[cyan]Insert you resolution between [/cyan][red]5-25[/red]\n")
res = input('>')

print(" ")
print(" ")
print("[cyan]Insert you image file between [/cyan][red] 'P'ng , 'J'pg , 'JP'eg , 'S'vg[/red]\n")
bye = "[#34c73e]Success![/#34c73e]"
test = input('>')
if test == 'P':
    print('creating...')
    fileext = "png"
    print(bye)
elif test == 'J':
    print('creating...')
    fileext = "jpg"
    print(bye)
elif test == 'JP':
    print('creating...')
    fileext = "jpeg"
    print(bye)
elif test == "S":
    print('creating...')
    fileext = "svg"
    print(bye)
    
# String which represents the QR code
s = link

# Generate QR code 
url = pyqrcode.create(s)

# Create and save the png file naming (smth).png 
url.png(f'{name}.{fileext}', scale = res)


# Success = Completed making QR code for you !!!

# Coded by ThomasAung#5599 on discord
