from collections import deque

def recurse_move(oldlist, stop, newlist):
    print newlist
    while len(newlist) < stop:
        newlist.append(oldlist.popleft())
        recurse_move(oldlist,stop,newlist)


oldlist=deque([1,2,3,4,5])
newlist=[]
stop=len(oldlist)

recurse_move(oldlist,stop,newlist)

print oldlist