def search(n,pt):
    file = open(f"C:\\Users\\madha\\PycharmProjects\\oeisVisualizer\\textDBData\\textDB{n}.txt","r+")
    fileRead = file.readlines()[0].split(" ,")[1]
    DataSrch = [x.split(", ") for x in fileRead.split("),(")]
    DataSrch[-1] = DataSrch[-1][:-3]
    index ={}
    Mindex =[]
    for i in DataSrch:
        if(len(i) == 0):
            continue
        if i[0] not in index:
            index [i[0]] = 1/(1 + float(i[1]))
            Mindex.append([i[0],int(i[1])])
        else:
            index[i[0]] += 1/(1 + float(i[1]))
            Mindex.append([i[0],int(i[1])])
    sortedDict=dict(sorted(index.items(), key=lambda item: item[1], reverse=True))
    if(pt):
        print(len(sortedDict))
        for s in sortedDict:
            print(s,sortedDict[s])
    return sorted(Mindex, key = lambda x:x[1])
def multisearch(items):
        Sitems = sorted(items,reverse = True)
        totDict=[]
        alr = []
        for it in Sitems:
            print(it)
            S = search(it,False)
            if(it == Sitems[0]):
                alr = [x[0] for x in S]
            else:
                Pt = {x[0]:True for x in S}
                alr = [x for x in alr if x in Pt]
        alr = {x: True for x in alr}
        print(len(alr))
        for it in items:
            print(it)
            S = search(it,False)
            if(len(S[0]) == 2):
                totDict += [[it] + x for x in S if x[0] in alr]
        totDict.sort(key = lambda x: x[2])
        T = len(totDict)
        combDict={}
        sortDict={}
        ref = []
        r = 0
        for t in totDict:
            r +=1
            if t[1] not in combDict and t[0] == items[0]:
                combDict[t[1]] = [t[2]]
                for i in range(len(items) - 1):
                    combDict[t[1]].append(-1)
            cr = items.index(t[0])
            if (t[1] not in combDict or cr != 0 and (combDict[t[1]][cr - 1] == -1)):
                continue
            combDict[t[1]][cr] = t[2]
            if(t[1] == "A260039"):
                print(combDict[t[1]])
            if (cr == len(items) - 1):
                if t[1] not in sortDict:
                    sortDict[t[1]] = 1 / float(t[2] + 1)
                else:
                    sortDict[t[1]] += 1 / float(t[2] + 1)
        sortedDict = dict(sorted(sortDict.items(), key=lambda item: item[1], reverse=True))
        print(len(sortedDict))
        for s in sortedDict:
            print(s, sortedDict[s])
multisearch([2,10,15])


