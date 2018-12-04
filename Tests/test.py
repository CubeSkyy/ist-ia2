import itertools

# n=2
# lst = map(list, itertools.product([0, 1], repeat=n))
# # lst = list(itertools.product([0, 1], repeat=n))
# for a in lst:
#     print(a)
#
# result = [(a, 1, 2, a, 4) for a in map(list, itertools.product([0, 1], repeat=n))]
#
# print(result)

# ev = list((-1,[],[],1,1))
#
# print(ev.index([]))
# ev[ev.index([])] = 2
# print(ev.index([]))
# ev[ev.index([])] = 2
# print(ev.index([]))

# RECURSION WITH LINEAR LIST


# def evCombAux(ev, i, res):
#     ev = list(ev)
#     index = ev.index([])
#     ev[index] = i
#     if [] not in ev:
#         res.append(ev)
#         return res
#     return evCombAux(ev, 0,res), evCombAux(ev, 1,res)
#
# def evComb(ev):
#     res = []
#     evCombAux(ev, 0, res)
#     evCombAux(ev, 1, res)
#     return res


# RECURSION WITH NESTED LISTS
# def evCombAux(ev, i):
#     ev = list(ev)
#     index = ev.index([])
#     ev[index] = i
#     if [] not in ev:
#         return ev
#     return [evCombAux(ev, 0), evCombAux(ev, 1)]
#
# def evComb(ev):
#
#     return [evCombAux(ev, 0), evCombAux(ev, 1)]


# ev = ([],[],[])
# a =evComb(ev)
# print(a)
