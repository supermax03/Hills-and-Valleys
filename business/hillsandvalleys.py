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



