filename = input()
with open(filename,"r")as ptr:
    Total=0
    countLines = 0
    for line in ptr.readlines():
        temp = int(line)
        Total += temp
        countLines += 1
    countLines += 1
    s = ((countLines)*(countLines+1))/2
    print(s - Total)

