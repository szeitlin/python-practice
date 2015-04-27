def recurse_copy(oldlist, stop, newlist, i):
    print i, newlist
    while len(newlist) < stop:
        i += 1
        newlist.append(oldlist[i])
        #oldlist.remove([oldlist[i]])
        recurse_copy(oldlist, stop, newlist, i)


oldlist = [1, 2, 3, 4, 5]
newlist = []
stop = len(oldlist)
i = -1

recurse_copy(oldlist, stop, newlist, i)

print oldlist
