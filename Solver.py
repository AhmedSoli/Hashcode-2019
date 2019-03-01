
def solve(photos,tags):
    slides = []
    for key,tag in enumerate(tags):
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
            elif len(photos[tag]['V'] == 1):
                one = photos[tag]['V'].pop()
                for tagTwo in tags[key+1:]:
                    if len(photos[tagTWo]['V']) > 1:
                        one = photos[tagTWo]['V'].pop()
                        two = photos[tagTWo]['V'].pop()
                        slide = {'tags': tagTWo,'id':(one['id'],two['id'])}
                        slides.append(slide)
    return slides