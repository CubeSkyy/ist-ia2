# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob

    
    def computeProb(self, evid):
        if len(self.parents) == 0:
            return 1-self.prob[0], self.prob[0]

        tempProb = self.prob
        tempParents = self.parents
        evTemp = evid[tempParents[0]]

        while (len(tempParents) > 1):
            tempProb = tempProb[evTemp]
            tempParents = tempParents[1:]
            evTemp = evid[tempParents[0]]

        return 1 - tempProb[evTemp], tempProb[evTemp]
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):
        evid = list(evid)
        index = evid.index(-1)

        evidAux = evid.copy()
        evidAux[index] = 0
        sum1=0
        for ele in self.evComb(evidAux):
            sum1 += self.computeJointProb(ele)

        evidAux = evid.copy()
        evidAux[index] = 1
        sum2 = 0
        for ele in self.evComb(evidAux):
            sum2 += self.computeJointProb(ele)


        alpha = 1/(sum1 + sum2)

        return alpha * sum2

    def computeJointProb(self, evid):
        temp = 1

        for i, val in enumerate(self.prob):
            temp *= val.computeProb(evid)[evid[i]]

        return temp

    def evCombAux(self,ev, i, res):
        ev = list(ev)
        index = ev.index([])
        ev[index] = i
        if [] not in ev:
            res.append(ev)
            return res
        return self.evCombAux(ev, 0,res), self.evCombAux(ev, 1,res)

    def evComb(self,ev):
        res = []
        self.evCombAux(ev, 0, res)
        self.evCombAux(ev, 1, res)
        return res




#######################
#        TESTS        #
#######################


gra = [[], [0], [0], [1, 2]]
ev = (1, 1, 1, 1)

p1 = Node(np.array([.5]), gra[0])  # cloudy
print("p1 false %.4e p1 true %.4e" % (p1.computeProb(ev)[0], p1.computeProb(ev)[1]))

p2 = Node(np.array([.5, .1]), gra[1])  # sprinkler

p3 = Node(np.array([.2, .8]), gra[2])  # rain

p4 = Node(np.array([[.0, .9], [.9, .99]]), gra[3])  # wetgrass
print("p2 = 1, p3 = 1, p4 false %.4e p4 true %.4e" % (p4.computeProb(ev)[0], p4.computeProb(ev)[1]))

prob = [p1, p2, p3, p4]

bn = BN(gra, prob)

jp = []
for e1 in [0, 1]:
    for e2 in [0, 1]:
        for e3 in [0, 1]:
            for e4 in [0, 1]:
                jp.append(bn.computeJointProb((e1, e2, e3, e4)))

print("sum joint %.3f (1)" % sum(jp))

### Tests to joint Prob
ev = (0, 0, 0, 0)
print("joint %.4g (0.2)" % bn.computeJointProb(ev))

ev = (1, 1, 1, 1)
print("joint %.4g (0.0396)" % bn.computeJointProb(ev))

### Tests to post Prob
# P(e1|e4=1)
ev = (-1, [], [], 1)
print("ev : ")
print(ev)
print("post : %.4g (0.5758)" % bn.computePostProb(ev))

# P(e4|e1=1)
ev = (1, [], [], -1)
print("ev : ")
print(ev)
print("post : %.4g (0.7452)" % bn.computePostProb(ev))

# P(e1|e2=0,e3=0)
ev = (-1, 0, 0, [])
print("ev : ")
print(ev)
print("post : %.4g (0.3103)" % bn.computePostProb(ev))