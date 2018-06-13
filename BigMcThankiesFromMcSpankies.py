import ev3dev.ev3 as ev3

ts = ev3.TouchSensor()
while true:
    m = ev3.MediumMotor('outB')

