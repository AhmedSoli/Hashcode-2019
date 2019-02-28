from collections import defaultdict

def get_buckets(photos):
    buckets = defaultdict(int)
    for photo in photos:
        buckets[len(photo['tags'])] = photo
    return buckets