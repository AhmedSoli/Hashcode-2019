from Score import * 

def solve(photos,tags):
    tags = sorted(tags.keys())
    slides = []
    for key,tags in enumerate(tags):
        while(True):
            if len(photos[tag]['H']) > 0:
                # handle horizontal photo
                slides.append(photos[tag]['H'].pop())
            else:
                # handle vertical photos
                if len(photos[tag]['V']) > 1:
                    one = photos[tag]['V'].pop()
                    two = photos[tag]['V'].pop()
                    slide = {'tags': tag,'id':(one['id'],two['id'])}
                    slides.append(slide)
                elif len(photos[tag]['V']) == 1:
                    one = photos[tag]['V'].pop()
                    for tagTwo in tags[key+1:]:
                        if len(photos[tagTwo]['V']) > 1:
                            one = photos[tagTwo]['V'].pop()
                            two = photos[tagTwo]['V'].pop()
                            slide = {'tags': tagTwo,'id':(one['id'],two['id'])}
                            slides.append(slide)
                else:
                    break

    return slides

def solve_alt(photos,tags):
    slides = []
    tags = sorted(tags.keys())
    print(tags)
    for key,tag in enumerate(tags):
        print(tag)
        while(True):
            if len(photos[tag]['H']) > 0:
                # handle horizontal photo
                if len(photos[tag]['H']) == 1: 
                    slides.append(photos[tag]['H'].pop())
                else:
                    one = photos[tag]['H'].pop()
                    slides.append(one)
                    best_score = -1
                    best_key = 0
                    for keyTwo,two in enumerate(photos[tag]['H']):
                        score = get_score(one,two)
                        if score > best_score:
                            best_score = score
                            best_key = keyTwo
                            # optimisation window
                            if best_score > int(tag / 2) - int(tag/5):
                                break
                    slides.append(photos[tag]['H'].pop(keyTwo))
            else:
                # handle vertical photos
                if len(photos[tag]['V']) > 1:
                    one = photos[tag]['V'].pop()
                    two = photos[tag]['V'].pop()
                    slide = {'tags': tag,'id':(one['id'],two['id'])}
                    slides.append(slide)
                elif len(photos[tag]['V']) == 1:
                    one = photos[tag]['V'].pop()
                    for tagTwo in tags[key+1:]:
                        if len(photos[tagTwo]['V']) > 1:
                            one = photos[tagTwo]['V'].pop()
                            two = photos[tagTwo]['V'].pop()
                            slide = {'tags': tagTwo,'id':(one['id'],two['id'])}
                            slides.append(slide)
                else:
                    break
    return slides
