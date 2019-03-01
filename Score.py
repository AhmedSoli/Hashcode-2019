def in_left_but_not_in_right(photoLeft, photoRight) -> int:
    return len(photoLeft['tag_ids'] - photoRight['tag_ids'])

def in_right_but_not_in_left(photoLeft, photoRight) -> int:
    return len(photoLeft['tag_ids'] - photoRight['tag_ids'])

def common_tag_ids(photoLeft, photoRight) -> int:
    return len(photoLeft['tag_ids'] & photoRight['tag_ids'])

def get_score(pL, pR) -> int:
    return min(common_tag_ids(pL, pR), in_left_but_not_in_right(pL, pR), in_right_but_not_in_left(pL, pR))
    