#!/usr/bin/python3
''' module for working using lockboxes
'''


def canUnlockAll(boxes):
    '''Passes on each box
    '''
    n = len(boxes)
    seen = set([0])
    unseen = set(boxes[0]).difference(set([0]))
    while 0 < len(unseen):
        boxIn = unseen.pop()
        if not boxIn or boxIn >= n or boxIn < 0:
            continue
        if boxIn not in seen:
            unseen = unseen.union(boxes[boxIn])
            seen.add(boxIn)
    return n == len(seen)
