from collections import defaultdict

def get_buckets(photos):
    buckets = defaultdict(list)
    for photo in photos:
        buckets[len(photo['tags'])].append(photo)
    return buckets

