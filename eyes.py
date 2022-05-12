import time
import winsound

class VisualUnit:
    def __init__(self):
        super().__init__()
        t1 = time.time()
        time.sleep(1)
        t2 = time.time() - t1
        seconds_left = []

        print(t2)
        while len(seconds_left) != 60*20:
            print(len(seconds_left) + 1)
            seconds_left.append(t2)
            time.sleep(1)
        else:
            print('Done',len(seconds_left))
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

app = VisualUnit()
