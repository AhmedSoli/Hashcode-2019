def in_left_but_not_in_right(photoLeft, photoRight) -> int:
    return len(photoLeft['tags'] - photoRight['tags'])

def in_right_but_not_in_left(photoLeft, photoRight) -> int:
    return len(photoLeft['tags'] - photoRight['tags'])

def common_tags(photoLeft, photoRight) -> int:
    return len(photoLeft['tags']) & photoRight['tags'])

def score(pL, pR) -> int:
    return min(common_tags(pL, pR), in_left_but_not_in_right(pL, pR), in_right_but_not_in_left(pL, pR))
    