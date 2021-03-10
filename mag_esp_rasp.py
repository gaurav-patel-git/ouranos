import serial, time, threading

baud_rate = 9600
timeout = 1
heading = 0

def sanetize_heading(head):
    global heading
    try:
        heading = int(head)
    except ValueError: 
        heading = int(head[0:2])
    except: 
        heading = int(head[0])
def get_mag_bearing():
    global heading
    while True:
        num = 0
        try:
            ser =  serial.Serial(f'/dev/ttyUSB{num}', baud_rate)
        except: 
            num += 1
            ser =  serial.Serial(f'/dev/ttyUSB{num}', baud_rate)
        try:
            line = str(ser.readline())
            print(line)
            head = line[2:5]
            # print(head, 'head')
            sanetize_heading(head)
            # heading = int(heading) if heading[0] != ':' else int(heading[1:])                
            print(heading)
        except: 
            print('Problem in getting degree')
            time.sleep(0.1)
        ser.close()


# get_mag_bearing()
threading.Thread(target=get_mag_bearing).start()
print('thread started for magnetometer')
# if __name__=="__main__":
#     while True:
#         print(heading)
        # time.sleep(1)