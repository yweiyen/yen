from machine import Timer

def callback1(t):
    print(1)
    
def callback2(t):
    print(2)
    
def callback3(t):
    print(3)
    t.deinit()

    
time1 = Timer()
time1.init(freq=1,callback=callback1)

time2 = Timer()
time2.init(freq=2000,callback=callback2)

time3 = Timer()
time3.init(freq=3000,callback=callback3)
