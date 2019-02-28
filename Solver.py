from Interpreter import parse,vertical_combinations
import itertools
import logging
import sys
from collections import Counter
from buckets import get_buckets
from score import score
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




if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error('wrong number of args')
        exit()
    photos = parse(sys.argv[1])
    horizontals = []
    verticals = []
    for photo in photos:
        if photo['direction'] == 'H':
            horizontals.append(photo)
        else:
            verticals.append(photo)

    buckets = get_buckets(horizontals)

    bucket_sizes = []
    for i, bucket in buckets.items():
        bucket_sizes.append((i, len(bucket)))

    sorted_bucket_keys = list(map(lambda x: x[0], sorted(bucket_sizes, key=lambda x: x[1], reverse=True)))

    pprint(buckets)
    for target_size in sorted_bucket_keys:
        (combinations, verticals) = vertical_combinations(target_size, verticals)
        for combination in combinations:
            buckets[len(combination['tags'])].append(combination)

    pprint(buckets)
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