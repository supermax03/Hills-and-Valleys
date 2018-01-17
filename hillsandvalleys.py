#####################################################
#Author: Maximiliano Bordon
#####################################################
def getgroundinfo(ground):
    isValley = 1
    isHill = 1
    count_valleys = 0
    count_hills = 0
    index = 1
    previous = ground[0]
    while (index < len(ground)):
        if (previous > ground[index]):
            isValley = 1
            if (isHill == 1):
                count_hills += 1
                isHill = 0
        if (previous < ground[index]):
            isHill = 1
            if (isValley == 1):
                count_valleys += 1
                isValley = 0
        previous = ground[index]
        index += 1
    if (isValley):
        count_valleys += 1
    else:
        if (isHill):
            count_hills += 1
    return (count_hills, count_valleys)


if __name__=='__main__':
       #ground = [0,1,0,1,0,-3,0]
       #ground=[1,0,1,1,1,0,1]
       #ground=[1,1,1,0,1]
       ground=[0,0,0,0,0,1]
       hills,valleys=getgroundinfo(ground)
       print("Hills-> {0}, Valleys ->{1}".format(hills,valleys))

