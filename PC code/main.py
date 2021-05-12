import serial

import restart_game
import interact_with_store
import autocart

ser = serial.Serial('COM5')
num_rounds = 2

for i in range(num_rounds):
    print('------------------------------')
    print('STARTING ROUND {:n} of {:n}'.format(i+1, num_rounds))
    restart_game.restart_game(ser)
    interact_with_store.go_to_store(ser, at_hub_entrance=False)
    interact_with_store.make_one_talisman(ser)
    autocart.autocart(ser, n=1)
    interact_with_store.go_to_store(ser)
    interact_with_store.check_talisman(ser, row_total=1, column_total=1)
    interact_with_store.take_all_and_leave(ser, row_total=1, column_total=1)
    restart_game.save_game(ser)
    interact_with_store.make_batch_talisman(ser, n=10)
    autocart.autocart(ser, n=10)
    interact_with_store.go_to_store(ser)
    interact_with_store.check_talisman(ser, row_total=5, column_total=10)
    print('FINISHED ROUND {:n} of {:n}'.format(i+1, num_rounds))
