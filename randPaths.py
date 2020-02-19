#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import copy


class randPaths:

    def __init__(self, GRAPH, NODES, startNode, endNode):
        self.GRAPH = GRAPH
        self.numberOfNodes = NODES
        self.startNode = startNode
        self.endNode = endNode
        self.route = []
        self.availableNodes = []

    def makeRoute(self):
        # create random path
        # create graph copy
        newGRAPH = copy.deepcopy(self.GRAPH)
        # initial route
        self.route = []
        # append start node
        self.route.append(self.startNode)

        # while last node is different from end node
        i = 0
        while self.route[-1] != self.endNode:
            self.availableNodes = []
            available = 0
            # loop through all nodes
            for j in range(self.numberOfNodes):
                if newGRAPH[self.route[-1]][j] > 0:
                    # add which nodes are available
                    self.availableNodes.append(j)
                    available += 1
            # loop through all nodes
            for k in range(self.numberOfNodes):
                newGRAPH[k][self.route[-1]] = 0
                newGRAPH[self.route[-1]][k] = 0

            if available == 0:
                i = 0
                self.route = []
                self.route.append(self.startNode)
                newGRAPH = copy.deepcopy(self.GRAPH)

            else:
                # create random route
                self.route.append(self.availableNodes[random.randint(0, available - 1)])
                i += 1

        return self.route
