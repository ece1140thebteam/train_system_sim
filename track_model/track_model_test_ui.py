from PyQt5.QtGui import QGuiApplication, QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, Qt, QModelIndex, QAbstractItemModel, pyqtProperty, pyqtSlot, pyqtSignal, QRunnable, QThreadPool, QThread
from PyQt5.QtWidgets import QFileDialog, QApplication

import sys 

import Track
import TrackBlock
import re
import csv 

class Gvars:
    input_type          = None
    input_field          = None
    current_update_type = None
    track_file          = None
    track               = Track.Track()

def get_track_file():
    with open('loaded_track', 'r') as f:
        Gvars.track_file = f.read()
        print(Gvars.track_file)

update_field = {
    "Authority": "Distance (feet)",
    "Commanded Speed": "Speed (mph)",
    "Switch Position": "Block number to switch to",
    "Railway Crossing": "Open or Closed",
    "Signal": "Red or Green",
    "Track Maintenance": "Yes or No",
    "Track Heater": "On or Off",
    "Track Failure": "Failure type (Broken Rail, Track Circuit failure, Power failure)",
    "Lights": "On or Off",
    "Track Circuit": "Open or Closed",
}

def parse_track():
    print(Gvars.track_file)
    get_track_file()

    with open(Gvars.track_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader, None)
        
        for block in reader:
            line = block[0]
            infra = block[6]

            inf_arr = infra.split(';')
            station = None
            underground = False
            switch = None
            railway_crossing = False
            block_travels_to = []
            
            for i in inf_arr:
                if 'RAILWAY' in i:
                    railway_crossing = True
                elif 'UNDERGROUND' in i:
                    underground = True
                elif 'Station' in i:
                    station = i
                elif 'Switch' in i:
                    # find all switch connections
                    all = [int(x) for x in re.findall(r'\d+', i.lower().replace('yard', '0'))]
                    if len(all) > 2:
                        start = int(max(set(all), key = all.count))
                        # to = [x for i, x in enumerate(all) if i!=start]
                        to = [x for x in all if x != start]
                        Gvars.track.add_switch(line, start, to)

            connections = block[10]
            connections = connections.split(';')

            # set switch connections within the block
            for c in connections:
                if '*' in c:
                    val = int(c.replace('*',''))
                    if switch is None:
                        switch = [val]
                    else:
                        switch.append(val)
                    block_travels_to.append(val*-1)
                else:
                    block_travels_to.append(int(c))
            
            b = TrackBlock.TrackBlock(
                line = line,
                section = block[1],
                block_number = block[2],
                block_len = block[3],
                block_grade = block[4],
                speed_limit = block[5],
                underground = underground,
                station = station,
                switch = switch,
                elevation = block[8],
                cum_elevation = block[9],
                has_rail_crossing = railway_crossing,
                can_travel_to = block_travels_to
            )

            # b.print()
            # print()

            Gvars.track.add_block(b)
    
    # Gvars.track.print()

def submit_update(update_type, target, value):
    print(f'{update_type} {target} {value}')

    with open('test_communications', 'w') as f:
        f.write(f'{update_type}:{target}:{value}')
    pass

class BooleanBinding(QObject):
    booleanChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._boolean = ""

    @pyqtProperty(bool, notify=booleanChanged)
    def boolean(self):
        return self._boolean

    @boolean.setter
    def boolean(self, value):
        if self._boolean == value:
            return
        self._boolean = value
        self.booleanChanged.emit()

    
class TextBinding(QObject):
    textChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._text = ""

    @pyqtProperty(str, notify=textChanged)
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if self._text == value:
            return
        self._text = value
        self.textChanged.emit()
 
class QFunctions(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(str)
    def update_command_type(self, command):
        print(command)
        Gvars.current_update_type = command

        Gvars.input_field.text = update_field[command]
        if command == "Commanded Speed" or command == "Authority":
            Gvars.input_type.text = "Train Number"
        elif command == "Track Maintenance":
            Gvars.input_type.text = "Section"
        else:
            Gvars.input_type.text = "Block Number"

        print(Gvars.input_type.text)
    
    @pyqtSlot(str, str)
    def send_update(self, target, value):
        print(f'{target} {value} ')
        line = list(Gvars.track.track_lines.values())[0] # TODO update this 
        
        if Gvars.input_type.text == "Section":
            if value not in line.sections:
                print('error: invalid section, reenter')
                return
        elif Gvars.input_type.text == "Train Number":
            try:
                train_num = int(target)
                submit_update(Gvars.current_update_type, target, value)
            except:
                print('error please enter a valid train number')
        else:
            try:
                block_num = int(target)

                if block_num < len(line.graph) and block_num > 0:
                    submit_update(Gvars.current_update_type, target, value)
                    return
                else:
                    print(f'{block_num}block number invalid')

            except:
                print('not an int')
            
        print("sending test")
        


def main():
    Gvars.function_bindings = QFunctions()
    Gvars.input_type        = TextBinding()
    Gvars.input_field        = TextBinding()
    
    parse_track()

    Gvars.app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("function_bindings", Gvars.function_bindings)
    engine.rootContext().setContextProperty("input_type", Gvars.input_type)
    engine.rootContext().setContextProperty("input_field", Gvars.input_field)

    engine.quit.connect(Gvars.app.quit)
    engine.load('./track_model_test.qml')

    sys.exit(Gvars.app.exec())
    

    
if __name__ == "__main__":
    main()