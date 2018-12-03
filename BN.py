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
        pass

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        pass
        
        return 0



