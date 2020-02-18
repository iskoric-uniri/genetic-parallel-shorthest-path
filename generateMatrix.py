import numpy as np
import csv

matrix = np.random.randint(0, 200, (200, 200))

i = 0
for row in matrix:
    row[i] = 0
    i = i+1

with open('connectedGraph.csv', mode='w') as graph_file:
    graph_writer = csv.writer(graph_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in matrix:
        graph_writer.writerow(row)
