PCBMotor.spinAtSpeed()
print(Hall.calcRPM())
PCBMotor.changeSpeed(Hall.calcRPM(), 1000)
print(Hall.calcRPM())