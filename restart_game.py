import serial
import time

def restart_game(ser):
    seq_close_game = b'HO0100ho1000XX0100xx0500AA0100aa0100'
    seq_start_game = b'AA0100aa1500AA0100aa0100'
    seq_enter_game = b'AA0100aa9000LN2000AA0100aa0500AA0100aa3000AA0100aa0100'

    print('Closing game...')
    ser.write(seq_close_game)
    time.sleep(7)
    print('Done')
    print('Starting game...')
    ser.write(seq_start_game)
    time.sleep(40)
    print('Done')
    print('Entering game...')
    ser.write(seq_enter_game)
    time.sleep(40)
    print('Done')

def save_game(ser):
    print('Saving...')
    seq_save_game = b'PL0100pl0100LE0100le0100DU0100du0100DU0100du0100AA0100aa0100DL0100dl0100AA0100aa0100'
    ser.write(seq_save_game)
    time.sleep(4)
    print('Done')
    
if __name__ == '__main__':
    ser = serial.Serial('COM5')
    restart_game(ser)
