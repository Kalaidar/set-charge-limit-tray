import pystray
from pystray import MenuItem as item
from PIL import Image
import subprocess

def set_charge_limit(icon, charge_percent, image):
    command = subprocess.getoutput("echo " + charge_percent + " | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold")
    icon.icon = image

def exit_application(icon, item):
    icon.stop()

image60 = Image.open("icons/60.png")
image80 = Image.open("icons/80.png")
image100 = Image.open("icons/100.png")
command = subprocess.getoutput("cat /sys/class/power_supply/BAT0/charge_control_end_threshold")
charge_limit = command
if charge_limit == "60":
    image = image60
if charge_limit == "80":
    image = image80
if charge_limit == "100":
    image = image100
    
menu = (
    item('Set charge limit to 100%', lambda: set_charge_limit(icon, "100", image100)),
    item('Set charge limit to 80%', lambda: set_charge_limit(icon, "80", image80)),
    item('Set charge limit to 60%', lambda: set_charge_limit(icon, "60", image60)),
    item('Exit', lambda: exit_application(icon, item))
)
icon = pystray.Icon("name", image, "Title", menu)

icon.run()