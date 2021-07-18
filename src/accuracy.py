import numpy as np

def accuracy(source_node,predicted_set):
    a = []
    for i in source_node:
        if i in predicted_set:
            a.append(1/(predicted_set[0]))
        else:
            a.append(0)
    acc = np.mean(a)
    return acc