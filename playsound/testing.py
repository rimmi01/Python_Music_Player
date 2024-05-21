from multiprocessing import Process
import time

def something():
    for x in range(10):
        print(x)
        time.sleep(1)
    return 0;



if __name__=="__main__":
    p1 = Process(target = something)
    p1.start()
    input()
