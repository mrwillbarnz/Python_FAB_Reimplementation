# Fancy Credits v2.0 
# Can run OS-agnostic, installs packages required to 
# \sound the system bell.
# Demonstrates escape sequences and utilising external modules.

# Is Sultan installed?



#Detecting OS routine (Which OS am I?)
import os 
import platform
print(os.name)

# Sounding the system bell routine (Windows-Only)
if condition:
print(platform.system()) = "Linux"
print(platform.system()) = "Darwin"

else:
import winsound
  duration =  1000 # milliseconds
  freq = 500 # Hz
  winsound.Beep(freq, duration)







