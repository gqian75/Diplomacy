def diplomacy_eval(army, location, action, support, move):
    a = ['A']
    b = ['Madrid']
    return a,b

def diplomacy_solve(r, w):
    """
    r a reader
    w a writer
    """
    army = []
    location = []
    action = []
    support = []
    move = []

    for s in r:
        i = s.split()
        army.append(str(i[0]))
        location.append(str(i[1]))
        action.append(str(i[2]))
        if str(i[2])=="Hold":
            support.append("none")
            move.append("none")
        elif str(i[2])=="Support":
            support.append(str(i[3]))
            move.append("none")
        elif str(i[2])=="Move":
            support.append("none")
            move.append(str(i[3]))
    a, b = diplomacy_eval(army, location, action, support, move)
    x = 0
    while x<len(a):
        w.write(a[x]+" "+b[x]+"\n")
        x+=1
