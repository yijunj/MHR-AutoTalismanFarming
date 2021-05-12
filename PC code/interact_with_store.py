import serial
import screenshot
import time
import datetime
import beep

def go_to_store(ser, at_hub_entrance=True):
    print('Going to store...')
    seq_back_to_hub = b'MI0100mi0100DU0100du0100AA0100aa0100'
    seq_walk_to_store = b'LU1000LN0000LL1500LN0000'
    if not at_hub_entrance:
        ser.write(seq_back_to_hub)
        time.sleep(2)
    ser.write(seq_walk_to_store)
    time.sleep(4)
    print('Done')

def check_talisman(ser, row_total=5, column_total=10):
    print('Checking talismans...')
    talisman_found_flag = False
    wanted_skill = 'Exploit 2'
    # wanted_skill = 'Resistance 1'

    # seq_back_to_hub = b'MI0100mi0100DU0100du0100AA0100aa0100'
    # seq_walk_to_store = b'LU1000LN0000LL1500LN0000'
    seq_check_talisman = b'AA0100aa1000DD0100dd0100DD0100dd0100AA0100aa0100DU0100du0100AA0100aa0100'
    seq_check_talisman_right = b'DR0100dr0100'
    seq_check_talisman_down = b'DD0100dd0100'

    # ser.write(seq_back_to_hub)
    # ser.write(seq_walk_to_store)
    # go_to_store(ser)
    ser.write(seq_check_talisman)

    time.sleep(2)
    f = open('talisman_history.txt', 'a')
    screenshot.init()
    f.write(str(datetime.datetime.now()))
    f.write('\n')

    for row in range(row_total):
        for column in range(column_total):
            time.sleep(3)
            skills = screenshot.get_skills()
            slots = screenshot.get_slots()
            print(skills + ', ' + slots)
            if wanted_skill in skills:
                # if '2' in slots or '3' in slots:
                beep.beep()
                talisman_found_flag = True
                input('Talisman found! Press any key to continue, or unplug USB... ')
            f.write(skills)
            f.write(', ')
            f.write(slots)
            f.write('\n')
            ser.write(seq_check_talisman_right)
        ser.write(seq_check_talisman_down)

    f.write('\n')
    f.close()
    time.sleep(3)
    print('Done')
    return talisman_found_flag

def take_all_and_leave(ser, row_total=1, column_total=1):
    print('Taking talisman...')
    down_num = 7 - row_total
    seq_take_all = b'DD0100dd0100' * down_num + b'AA0100aa0100BB0100bb0100BB0100bb0100'
    ser.write(seq_take_all)
    time.sleep(3)
    print('Done')

def make_batch_talisman(ser, n=10):
    print('Making talismans...')
    seq_choose_pot = b'AA0100aa1000DD0100dd0200DD0100dd0200AA0100aa0200DD0100dd0200DD0100dd0200DD0100dd0200'
    seq_enter_melding = b'AA0100aa0200'

    ser.write(seq_choose_pot)
    time.sleep(3)

    for i in range(n):
        ser.write(seq_enter_melding)
        time.sleep(1)
        counter = 0
        while not screenshot.get_talisman_status('last'):
            counter += 1
            seq_submit_materials = b'AA0100aa0200DD0200dd3000AA0100aa0200DD0100dd0200'
            ser.write(seq_submit_materials)
            time.sleep(6)

        seq_move_cursor = b'DD0100dd0200' * (7-counter)
        ser.write(seq_move_cursor)
        time.sleep(3)
        seq_confirm = b'AA0100aa0200DL0100dl0500AA0100aa0200'
        ser.write(seq_confirm)
        time.sleep(2)

    seq_leave = b'BB0100bb0500BB0100bb0200'
    ser.write(seq_leave)
    time.sleep(3)
    print('Done')

def make_one_talisman(ser):
    print('Making one talisman...')
    seq_choose_pot = b'AA0100aa1000DD0100dd0200DD0100dd0200AA0100aa0200DD0100dd0200DD0100dd0200DD0100dd0200'
    seq_enter_melding = b'AA0100aa0200LE0100le0200LE0100le0200LE0100le0200LE0100le0200'

    ser.write(seq_choose_pot)
    time.sleep(3)

    ser.write(seq_enter_melding)
    time.sleep(3)
    counter = 0
    while not screenshot.get_talisman_status('first'):
        counter += 1
        seq_submit_materials_for_one = b'AA0100aa0200DU0200du1000AA0100aa0200DD0100dd0200'
        ser.write(seq_submit_materials_for_one)
        time.sleep(4)

    seq_move_cursor = b'DD0100dd0200' * (7-counter)
    ser.write(seq_move_cursor)
    time.sleep(3)
    seq_confirm = b'AA0100aa0200DL0100dl0500AA0100aa0200'
    ser.write(seq_confirm)
    time.sleep(2)

    seq_leave = b'BB0100bb0500BB0100bb0200'
    ser.write(seq_leave)
    time.sleep(3)
    print('Done')

if __name__ == '__main__':
    ser = serial.Serial('COM5')
    check_talisman(ser)
