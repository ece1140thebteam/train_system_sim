import mysql.connector
import pandas as pd
import xlrd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P1ttsburgh",
    database="ctcoffice"
)

query = "INSERT INTO track_blocks VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

mycursor = mydb.cursor()

print("Deleting all rows from track_blocks")
mycursor.execute("DELETE FROM track_blocks")

print("Adding Red Line")
redline = pd.read_excel('DataFiles/Track Layout & Vehicle Data vF.xlsx', sheet_name=1, usecols=['Line', 'Section', 'Block Number', 'Infrastructure'])
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
redline = pd.read_excel('DataFiles/Track Layout & Vehicle Data vF.xlsx', sheet_name=2, usecols=['Line', 'Section', 'Block Number', 'Infrastructure'])
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

mydb.commit()





