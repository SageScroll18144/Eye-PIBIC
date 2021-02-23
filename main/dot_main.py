import dot

obj = dot.Dot()

while True:
    if obj.EventMovement():
        obj.move_dot()  
    if obj.isToClose():
        break

obj.exit_window()