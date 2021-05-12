import winsound

def beep(freq=440, dura=1000):
    winsound.Beep(freq, dura)

if __name__ == '__main__':
    beep()
