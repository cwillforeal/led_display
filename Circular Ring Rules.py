"""artificially arrange items in a cirlce, and initiate a rule that turns an item on
if both its neighbors are turned on, and turns it off if only 1 neighbor is on.
Initial configuration of on/off is 'random' The below script is used to update
the values in a list which should correspond to the LED lights on a light ring.
The parameters and rules can be updated and changed to be whatever is needed."""

import random
print("looplist")
loopedlist = []
for x in range(20):
  loopedlist.append(random.randint(0, 1))
print('Original configuration of the loopedlist is {}'.format(loopedlist))


"""This code looks at the neighbor two spaces in front of 
the curent index and if that LED light has the same value (on or off) then 
the current index will switch from on to off or vice versa"""
def twoahead(list):
    loopedlist = list
    key = 2
    p = 0
    numofruns = 5
    while p <= numofruns:
        for i in range(len(loopedlist)):
            index = (i+key)%len(loopedlist)
            if loopedlist[i] == loopedlist[index]:
              # if loopedlist[i] == 0:
              #     loopedlist[i] = 1
              # elif loopedlist[i] == 1:
              #     loopedlist[i] = 0
                loopedlist[i] = int(not loopedlist[i])
            print(loopedlist) #if i change indentation it will only print after going through all items in the list rather than printing after it goes through each item
        p += 1
"""these rules check if the neighbor two behind of the current index is the same"""
def twobehind(list):
    loopedlist = list
    key = 2
    p = 0
    numofruns = 5
    while p <= numofruns:
        for i in range(len(loopedlist)):
          index = (i-key) % len(loopedlist)
          if loopedlist[i] == loopedlist[index]:
              loopedlist[i] = int(not loopedlist[i])
          #print(loopedlist)
        p += 1


"""these rules check if the neighbor two ahead and two behind are the same and if so
the value will switch from 1 to 0 or vice versa."""
def equaltobothneighbors(list):
    loopedlist = list
    #loopedlist = [1,1,0,1,0,0,1,1,0,0,0,0] this configuration will not enduce any changes
    key = 2
    p = 0
    numofruns = 5
    while p <= numofruns:
        for i in range(len(loopedlist)):
          forwardindex = (i+key) % len(loopedlist)
          previousindex = (i-key) % len(loopedlist)
          if loopedlist[i] == loopedlist[forwardindex] and loopedlist[i] == loopedlist[previousindex]:
              loopedlist[i] = int(not loopedlist[i])
          print(loopedlist)
        p += 1
        """very interesting results, the numbers clump into pairs of 1s and 0s no
        matter what the initial configuration is"""

"""If both immmediate neighbors are off (0), turn on (1)"""
def switchifneighborsoff(list):
    loopedlist = list
    key = 1
    p = 0
    numofruns = 5
    print("If immediate neighbors are off, turn on")
    while p <= numofruns:
        for i in range(len(loopedlist)):
          forwardindex = (i+key) % len(loopedlist)
          previousindex = (i-key) % len(loopedlist)
          if loopedlist [i] == 0 and loopedlist[forwardindex] == 0 and loopedlist[previousindex] == 0:
              loopedlist[i] = 1
          print(loopedlist)
        p += 1



"""A second method to check the value of the neighbors
and update if value is the same - I don't fully understand how it works"""
l = [0, 1, 0]
n = 0
while n < 2:  # choose number of iterations
    for i in range(len(l)):
        l[i] = (l[i], int(not l[i]))[l[i] == l[(i+2)%len(l)]]  # invert when equal to its neighbor
        #print(l)
    n += 1

equaltobothneighbors(loopedlist)
