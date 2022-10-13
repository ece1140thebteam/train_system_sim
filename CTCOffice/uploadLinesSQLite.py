import mysql.connector
import pandas as pd
import xlrd
import sqlite3

mydb = sqlite3.connect("ctcOffice.db")

query = "INSERT INTO track_blocks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

mycursor = mydb.cursor()

print("Deleting all rows from track_blocks")
mycursor.execute("DELETE FROM track_blocks")

file_name = 'DataFiles/Track Layout & Vehicle Data vF2.xlsx'

print("Adding Red Line")
redline = pd.read_excel(file_name, sheet_name=2, usecols=['Line', 'Section', 'Block Number', 'Infrastructure'])
for r in range(0, 76):
    line = str(redline.iloc[r]['Line'])
    section = str(redline.iloc[r]['Section'])
    blockNum = str(int(redline.iloc[r]['Block Number']))

    if str(redline.iloc[r]['Infrastructure']) == 'nan':
        Infrastructure = ''
    else:
        Infrastructure = str(redline.iloc[r]['Infrastructure'])
    values = (blockNum, line, section, 0, Infrastructure, '', None, 0, None)
    mycursor.execute(query, values)

print("Adding Green Line")
redline = pd.read_excel(file_name, sheet_name=3, usecols=['Line', 'Section', 'Block Number', 'Infrastructure'])
for r in range(0, 150):
    line = str(redline.iloc[r]['Line'])
    section = str(redline.iloc[r]['Section'])
    blockNum = str(int(redline.iloc[r]['Block Number']))

    if str(redline.iloc[r]['Infrastructure']) == 'nan':
        Infrastructure = ''
    else:
        Infrastructure = str(redline.iloc[r]['Infrastructure'])
    values = (blockNum, line, section, 0, Infrastructure, '', None, 0, None)
    mycursor.execute(query, values)

print("Adding Blue Line")
blueLine = pd.read_excel(file_name, sheet_name=1, usecols=['Line', 'Section', 'Block Number', 'Infrastructure'])
for r in range(0, 15):
    line = str(blueLine.iloc[r]['Line'])
    section = str(blueLine.iloc[r]['Section'])
    blockNum = str(int(blueLine.iloc[r]['Block Number']))

    if str(blueLine.iloc[r]['Infrastructure']) == 'nan':
        Infrastructure = ''
    else:
        Infrastructure = str(blueLine.iloc[r]['Infrastructure'])
    values = (blockNum, line, section, 0, Infrastructure, '', None, 0, None)
    mycursor.execute(query, values)


mydb.commit()





