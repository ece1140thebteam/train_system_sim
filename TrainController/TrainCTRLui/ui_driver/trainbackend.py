#Class for Train Data

class Train_CTRL_BE():

    def __init__(self, signals):
#Initialization of internal variables
        self.sigs = signals
        
        self.Kp = 35
        self.Ki = 1

        self.maxPow = 120000 #120kW, per the Datasheet
        self.powOutput = 0
        self.temp = 70
        self.auth = True
        self.cmdSpd = 0
        self.curSpd = 0
        self.speedLim = 70
        self.driverCmd = 0
        self.dispatch = False
        self.manMode = False
            
        self.engineFault = False
        self.trackSigFault = False
        self.brakeFault = False
        self.faultMode = False
        self.faultMessage = None
        
        #Convention: False = Closed/Off
        self.ldoors = False
        self.rdoors = False
        self.elights = False
        self.ilights = False

        self.station = None
        self.side = None
        self.beacon = None

        self.sBrake = False
        self.eBrake = False

    #Signals
        self.sigs.send_TrainCtrl_speed.connect(self.curSpdAdjust)
        self.sigs.send_TrainCtrl_failure.connect(self.failHandle)
        self.sigs.send_TrainCtrl_eBrake.connect(self.passEBrake)
        self.sigs.send_TrainCtrl_lights.connect(self.autoLights)

    def autoLights(self, lightState):
        self.eLights = lightState
        self.iLights = lightState


    def passEBrake(self):
        self.eBrake = True

    def beaconHandler(self, info):
        if info['beacon'] is not None:
            self.beacon = info['beacon']
            self.side = self.beacon['station_side']
            self.station = self.beacon['station_name']

    def failHandle(self, failActive, failType): 
            self.failMode = failActive
            if failType == 'Engine':
                self.engineFault = True
            elif failType == 'Brake':
                self.brakeFault = True
            elif failType == 'Signal':
                self.trackSigFault = True
            else:
                self.engineFault = False
                self.brakeFault = False
                self.trackSigFault = False


    #Function to adjust commanded speed, is called externally
    def cmdSpdAdjust(self, info):
        self.cmdSpd = info['commanded_speed']
        self.auth = info['authority']
        self.dispatch = True
        self.beaconHandler(info)
        self.powerCalc()
    
    #Function to adjust current speed, is called externally
    def curSpdAdjust(self, spd):
        self.curSpd = spd
        self.powerCalc()

    #Door functions
    def rDoors(self):
        self.sigs.send_TrainModel_rDoor.emit(self.rdoors)
    def lDoors(self):
        self.sigs.send_TrainModel_lDoor.emit(self.ldoors)

    #Light functions
    def eLights(self):
        self.sigs.send_TrainModel_eLight.emit(self.elights)
    def iLights(self):
        self.sigs.send_TrainModel_iLight.emit(self.ilights)

    #Temp function
    def tempAdjust(self):
        self.sigs.send_TrainModel_temp.emit(self.temp)

    #Brake Functions
    def sBrakeSig(self):
        self.sigs.send_TrainModel_sBrake.emit(self.sBrake)

    def eBrakeSig(self):
        self.sigs.send_TrainModel_eBrake.emit(self.eBrake)

    #Major Power calculation and Velocity adjustment method
    def powerCalc(self):
        if self.auth:
            if self.faultMode: #First checking for faults
                if self.trackSigFault or self.engineFault or self.brakeFault:
                    self.powOutput = 0
                    self.eBrake = True
                    #Send brake states to Train Model and display popup to user indicating fault
                    self.sigs.send_TrainModel_eBrake.emit(self.eBrake)
                    #self.sigs.send_TrainModel_sBrake.emit(self.sBrake)

            else: #No Faults Found
                if self.manMode: #Base calculation on driver set speed if in manual mode
                    error_k = self.driverCmd/2.23694 - self.curSpd
                else: #Automatic mode case
                    error_k = self.cmdSpd*0.277778 - self.curSpd


                pow = self.Kp * error_k + self.Ki * self.curSpd

                #Automatic mode handling
                if not self.manMode:
                    #If power becomes negative, set to 0 and engage SBrake
                    if pow < 0:
                        pow = 0
                        if self.dispatch == True:
                            self.sBrake = True
                            self.sigs.send_TrainModel_sBrake.emit(self.sBrake)
                    else:
                        if self.sBrake:
                            self.sBrake = False


                #Check to make sure max power is not exceeded
                if pow > self.maxPow:
                    pow = self.maxPow

                #Set power to 0 if brakes active
                if self.eBrake or self.sBrake:
                    pow = 0
                    if self.eBrake:
                        self.sBrake = False
                        #Send Brake State signals to train model
                        #self.sigs.send_TrainModel_eBrake.emit(self.eBrake)
                        #self.sigs.send_TrainModel_sBrake.emit(self.sBrake)
                    elif self.sBrake:
                        self.eBrake = False
                        #Send Brake State signals to train model
                        #self.sigs.send_TrainModel_eBrake.emit(self.eBrake)
                        #self.sigs.send_TrainModel_sBrake.emit(self.sBrake)
                    else:
                        print('No Brakes Enabled, calculating power...')
                else:
                    pass
                    #self.sigs.send_TrainModel_eBrake.emit(self.eBrake)
                    #self.sigs.send_TrainModel_sBrake.emit(self.sBrake)      
                
                self.powOutput = pow
                self.sigs.send_TrainModel_powerOutput.emit(self.powOutput)

        else:
            self.sBrake = True
            self.sigs.send_TrainModel_sBrake.emit(self.sBrake) 
            self.powOutput = 0
            self.sigs.send_TrainModel_powerOutput.emit(self.powOutput)       
    