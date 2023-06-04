import os

dataFile = os.path.abspath("SaveData.txt")

def saveData(d,h, m, s, hu, j,b):
    open(dataFile, 'w').close()
    f = open(dataFile, 'w')
    f.write(str(d) + "\n")
    f.write(str(h) + "\n")
    f.write(str(m) + "\n")
    f.write(str(s) + "\n")
    f.write(str(hu) + "\n")
    f.write(str(j) + "\n")
    f.write(str(b) + "\n")
    f.write("First row is the Day, Second is Health, Third is Money, Fourth is Sleep, Fifth is Hunger, Sixth is Job, Seventh is the bed currently owned")
    f.close()

def loadData():
    f = open(dataFile, "r")
    d = int(f.readline())
    h = int(f.readline())
    m = int(f.readline())
    s = int(f.readline())
    hu = int(f.readline())
    j = int(f.readline())
    b = int(f.readline())
    f.close()
    return [d,h,m,s,hu,j,b]

def deleteData():
    saveData(1, 100, 200, 100, 100, 0, 0)

#resetData()
#If the saving ever breaks just remove the hashtag above beside resetData then run this exact script. After you do that add the hashtag back.