from Interpreter import parse
import itertools
import logging
import sys
from collections import Counter
from buckets import get_buckets
from pprint import pprint

def sort_for_orientation(photos):
    h = list()
    v = list()
    for p in photos:
        if p['direction'] == 'H':
            h.append(p)
        else:
            v.append(p)
    return {'H': h, 'V': v}


def in_left_but_not_in_right(photoLeft, photoRight) -> int:
    return len(set(photoLeft['tags']) - set(photoRight['tags']))

def in_right_but_not_in_left(photoLeft, photoRight) -> int:
    return len(set(photoLeft['tags']) - set(photoRight['tags']))

def common_tags(photoLeft, photoRight) -> int:
    return len(set(photoLeft['tags']) & set(photoRight['tags']))

def score(pL, pR) -> int:
    return min(common_tags(pL, pR), in_left_but_not_in_right(pL, pR), in_right_but_not_in_left(pL, pR))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error('wrong number of args')
        exit()
    photos = parse(sys.argv[1])
    
    pprint(get_buckets(photos))
    #oriented = sort_for_orientation(photos)
    #c = Counter(map(lambda x: len(x['tags']), photos))
    #print(c)
    ## combinations for horizontal, permutations for vertical
    #hCombinations = itertools.combinations(oriented['H'], 2)
    #for comb in hCombinations:
    #    s = score(*comb)
    #    #if s > 0:
    #    #    print(f'h: {s}')
    #vCombinations = itertools.permutations(oriented['V'], 2)
    #for comb in vCombinations:
    #    s = score(*comb)
    #    #if s > 0:
    #    #    print(f'v: {s}')

    #print(oriented)