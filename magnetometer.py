import py_qmc5883l
import time
sensor = py_qmc5883l.QMC5883L()
while True:
    m = sensor.get_bearing()
    print(m)
    time.sleep(0.1)