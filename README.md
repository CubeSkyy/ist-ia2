# Artificial Intelligence Second Project
Project for the 2018-2019 Artificial Intelligence Course in Instituto Superior Técnico.

This project had two parts: Bayesian Inference and Reinforcement Learning.

## Bayesian Inference
Goals:
* The data structure to support a baysian network was created (in the BN class)
* computeJointProb function that computes  the joint probability given a specific evidence (with no unknown values)
* computePostProb function that computes the a-posteriori probability of a variable given a specific evidence

Examples:

```python
ev = (1,1,1,1,1)
jp = []
for e1 in [0,1]:
  for e2 in [0,1]:
    for e3 in [0,1]:
      for e4 in [0,1]:
        for e5 in [0,1]:
          jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))
print("sum joint %.3f (1)" % sum(jp))
>>>
sum joint 1.000 (1)
```
```python
ev = (-1,[],[],1,1)
print( "post : %.4g (0.2842)" % bn.computePostProb(ev) )
>>>
post : 0.2842 (0.2842)
```

## Reinforcement Learning
Goals:
* Classic tabular Q-learning
* Functions that return exploration and exploitation (optimal) policies.
* Function that generates the optimal trajectory, given a start state and exploitation policy.

More info can be found in "Project2.pdf"
