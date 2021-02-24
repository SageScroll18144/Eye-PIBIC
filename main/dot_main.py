import dot
import time

to = time.time()
print("Time init: ", to)
obj = dot.Dot()

while True:
    if obj.EventMovement():
        obj.move_dot()  
        print("Tempo percorrido até o click(s): ", time.time()-to)
    if obj.isToClose():
        break

obj.exit_window()