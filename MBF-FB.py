import os, sys
#try:os.system('xdg-open https://youtube.com/@Niki404-Cyber')
except:pass
try:
    __import__("MBF-FB").login()
except Exception as e:
    exit(str(e))
