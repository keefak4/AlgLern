def cor(i):
    i = 4
    print i
    if i <= 0:
        return
    else:
    cor n(i - 1)
///////////////////////
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key")
            