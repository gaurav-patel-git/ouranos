from helper import Agrobot
# from mag_esp_rasp import bot.headingmport threading, time
import RPi.GPIO as GPIO
import serial, time, threading, copy



instruction = 's'
bot = Agrobot()

def ins_change(bot):
    bot.move('s')
    time.sleep(0.1)


def test_rotation(ins, rotat_dur, stop_dur):
    global instruction, heading
    heading = bot.heading
    cur_read, prv_read = bot.heading, 0
    print('Initial magnetometer reading is = ', cur_read)
    time.sleep(2)
    rotation_his = []
    while True:
        instruction = ins
        print(f'turning right for {rotat_dur}')
        time.sleep(rotat_dur)
        prv_read = copy.deepcopy(cur_read)
        cur_read = bot.heading
        # cur_read = bot.bot.heading
        rotation_degree = prv_read-cur_read
        print(f'Bot has turned {rotation_degree} degree from previous postion in {rotat_dur} seconds')
        print(f'cur head {bot.heading} coords {bot.position} ')
        rotation_his.append(rotation_degree)
        print(rotation_his)
        instruction = 's'
        print(f'stopped for {stop_dur}')
        time.sleep(stop_dur)

x = threading.Thread(target=test_rotation, args=('l', 1, 2))
x.start()
while True:
    bot.move(instruction)
