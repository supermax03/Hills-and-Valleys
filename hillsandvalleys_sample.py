from business.hillsandvalleys import getgroundinfo

if __name__=='__main__':
       #ground = [0,1,0,1,0,-3,0]
       #ground=[1,0,1,1,1,0,1]
       #ground=[1,1,1,0,1]
       ground=[0,0,0,0,0,1]
       hills,valleys=getgroundinfo(ground)
       print("Hills-> {0}, Valleys ->{1}".format(hills,valleys))

