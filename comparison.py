
from Score import *

def comparison(bucket):
    mean_length=0
    sum_len=0
    score = 0
    for length, photos in bucket.items():
        sum_len+= length

    mean_length = int(sum_len/len(bucket))

    while(1):
        if mean_length is in bucket.keys():
            break
        else:
            mean_length+=1
    out_list=[]
    first = bucket[mean_length].pop()
    while(len(bucket[mean_length])!=0) :

        for photo in bucket[mean_length]:
            score = get_score(first,photo)

            if score >= (mean_length/2-1):
                out_list.append(photo)
                first = photo
                break













