from gps import get_cord
import threading, time
    


time_duration = 1
latest_lat, latest_lng = 0,0
latest_bearing = 0



def get_latest_cord(time_duration):
    global latest_lat, latest_lng
    while True:
        latest_lat, latest_lng = get_cord()
        print('Cordinates', latest_lat, latest_lng)
        time.sleep(time_duration)

def get_latest_bearing(time_duration):
    global latest_bearing
    while True:
        latest_bearing = get_mag_bearing()
        print('Bearing', latest_bearing)
        time.sleep(time_duration)

gps_thread = threading.Thread(target=get_latest_cord, args=(time_duration,))
mag_thread = threading.Thread(target=get_latest_bearing, args=(time_duration,))
gps_thread.start()
mag_thread.start()