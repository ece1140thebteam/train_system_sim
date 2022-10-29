from LineInfo import LineInfo
from Blocks import Blocks
import pandas as pd
from BlockInfo import BlockInfo

file_name = 'DataFiles/Track Layout & Vehicle Data vF2.xlsx'


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

        print(lines[0].get(1).failure)

        return lines

        