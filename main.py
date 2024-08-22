from adb import *
import threading
from sheet import *
from PyQt5.QtCore import QThread
counter=0
tools=[]
devices=[]
spell=False
pkgame="com.riotgames.mobile.leagueconnect"
pkgame2="com.riotgames.mobile.leagueconnect/com.riotgames.mobile.leagueconnect.ui.MainActivity"
# Tạo một Lock object
file_lock = threading.Lock()
