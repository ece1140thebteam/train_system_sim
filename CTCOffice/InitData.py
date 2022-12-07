import pandas as pd

from CTCOffice.BlockInfo import BlockInfo
from CTCOffice.Blocks import Blocks
from CTCOffice.LineInfo import LineInfo

file_name = 'CTCOffice/DataFiles/Track Layout & Vehicle Data vF2.xlsx'


class InitData(): 
    def get_throughput(self):
        throughputs = []
        throughputs.append(LineInfo("Red"))
        throughputs.append(LineInfo("Green"))
        throughputs.append(LineInfo("Blue"))
        return throughputs;

    def get_blocks(self):
        lines = []
        blocks = {}
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

            block = BlockInfo()
            block.set_data(blockNum, line, section, Infrastructure)
            blocks[int(blockNum)] = block
        
        lines.append(blocks)

        blocks = {}
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
            
            block = BlockInfo()
            block.set_data(blockNum, line, section, Infrastructure)
            blocks[int(blockNum)] = block
        
        lines.append(blocks)

        return lines

    def get_lengths(self, line):
        blocks = {}
        if line == 'Green':
            green_line = pd.read_excel(file_name, sheet_name=3, usecols=['Block Length (m)'])
            for r in range(0, 150):
                length = (green_line.iloc[r]['Block Length (m)'])
                blocks[r+1] = length

        if line == 'Red':
            red_line = pd.read_excel(file_name, sheet_name=2, usecols=['Block Length (m)'])
            for r in range(0, 76):
                length = (red_line.iloc[r]['Block Length (m)'])
                blocks[r+1] = length
        return blocks

    def get_speeds(self, line):
        blocks = {}
        if line == 'Green':
            green_line = pd.read_excel(file_name, sheet_name=3, usecols=['Speed Limit (Km/Hr)'])
            for r in range(0, 150):
                length = (green_line.iloc[r]['Speed Limit (Km/Hr)'])
                blocks[r+1] = length

        if line == 'Red':
            red_line = pd.read_excel(file_name, sheet_name=2, usecols=['Speed Limit (Km/Hr)'])
            for r in range(0, 76):
                length = (red_line.iloc[r]['Speed Limit (Km/Hr)'])
                blocks[r+1] = length
        return blocks