import gspread
from gspread_formatting import *
gc = gspread.service_account(filename='serect.json')
from adb import sheetid,indexsheet
SPREADSHEET_ID = sheetid
indexsheet=indexsheet
sht1 = gc.open_by_key(SPREADSHEET_ID)
worksheet = sht1.get_worksheet(int(indexsheet))
