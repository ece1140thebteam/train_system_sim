import pandas as pd

from CTCOffice.BlockInfo import BlockInfo
from CTCOffice.Blocks import Blocks
from CTCOffice.LineInfo import LineInfo
from pathlib import Path

file_name = './CTCOffice/DataFiles/Track Layout & Vehicle Data vF2.xlsx'

file_name = str(Path(__file__).resolve().parent / "DataFiles"/ "Track Layout & Vehicle Data vF2.xlsx")

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

        