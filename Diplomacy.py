def diplomacy_eval(army, location, action, support, move):
    a = [] # army output
    b = [] # status output
    output = []
    p = [] #new positions
    x = 0
    power = [] #power of each army (support)
    while x<len(army):
        temp = []
        temp.append(army[x])
        temp.append(1)
        power.append(temp) # add each army with powerlevel
        a.append(army[x])
        #invalidate support
        if action[x]=="Support":
            sLoc = location[x] # support location
            for i in move:
                if i==sLoc:
                    action[x]="Hold" # if support being attacked, invalidate support
        x+=1

    x = 0
    while x<len(army):
        # calculate power (support)
        if action[x]=="Support":
            armySupported = support[x]
            for i in power:
                if i[0]==armySupported:
                    i[1]+=1 # add support
        #calculate new positions
        if action[x]=="Hold" or action[x]=="Support":
            l = location[x]
        elif action[x]=="Move":
            l = move[x]

        inserted = False
        for i in p:
            if i[0] == l:
                i.append(army[x])
                inserted = True
        if (inserted==False):
            temp = []
            temp.append(l)
            temp.append(army[x])
            p.append(temp)
        x+=1

    for i in p:
        if len(i)>2:
            #battle
            armies = [] # ARMIES IN THE BATTLE
            y = 1
            while y<len(i):
                armies.append(i[y])
                y+=1
            max = 0
            for j in armies:
                for z in power:
                    if j==z[0]:
                        armypowerlevel = z[1]
                if armypowerlevel > max:
                    max = armypowerlevel
            maxarmies = 0
            for j in armies:
                for z in power:
                    if j==z[0]:
                        armypowerlevel = z[1]
                if armypowerlevel==max:
                    maxarmies+=1
            if maxarmies==1: # 1 survive
                for j in armies:
                    for z in power:
                        if j==z[0]:
                            armypowerlevel = z[1]
                    if armypowerlevel<max:
                        output.append(j+" [dead]")
                    else:
                        output.append(j+" "+i[0])




            else: # everyone destroyed
                for j in armies:
                    output.append(j+" [dead]")



        elif len(i)==2:
            output.append(i[1]+" "+i[0])
    return output


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
    output = diplomacy_eval(army, location, action, support, move)
    for i in output:
        w.write(i+"\n")
