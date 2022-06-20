#Grupo: 21 Alunos: 87687 - Miguel Coelho; 87700 - Ricardo Silva

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

