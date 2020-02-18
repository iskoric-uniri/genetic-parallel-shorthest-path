#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import randPaths
import genes
from mpi4py import MPI


# Initial conditions
ITERATION = 5
CHILDREN = 20
MUT = 25
GRAPH = [[]]
NODES = 0


startNode = 14
endNode = 62

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    n = ITERATION
else:
    n = None

n = comm.bcast(n, root=0)

with open('connectedGraph.csv', "rt") as f:
    reader = csv.reader(f)
    for line in reader:
        for x in range(len(line)):
            GRAPH[NODES].append(int(line[x]))
        if NODES > 0:
            GRAPH[NODES].remove(NODES)
        NODES += 1
        GRAPH.append([NODES])

GRAPH.pop()
paths = randPaths.randPaths(GRAPH, NODES, startNode, endNode)
firstParent = paths.makeRoute()
secondParent = paths.makeRoute()

gen = genes.Genes(GRAPH, ITERATION, NODES, CHILDREN, MUT, startNode, endNode, firstParent, secondParent)
gen.makeRoute()
cost = gen.costOfBestRoute

minCost = comm.reduce(cost, op=MPI.MIN, root=0)
maxCost = comm.reduce(cost, op=MPI.MAX, root=0)
sumCost = comm.reduce(cost, op=MPI.SUM, root=0)
if rank == 0:
    print('Average cost: ', sumCost/size)
    print('Max cost: ', maxCost)
    print('Min cost: ', minCost)