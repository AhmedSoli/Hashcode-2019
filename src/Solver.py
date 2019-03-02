from Slide import * 
from Score import * 
from random import *


class Solver:
    def __init__(self,photos,tags):
        self.photos = photos
        self.tags = sorted(tags.keys())
        self.count_photos = 0
        for (key,val) in sorted(tags.items(),key=lambda x: x[1]['H'] + x[1]['V']):
            print(key,val)
            self.count_photos += val['H'] + val['V']

    # simple but fast solution
    def solve(self):
        slides = []

        for key,tag in enumerate(self.tags):
            while(len(self.photos[tag]['H']) > 0):
                # handle horizontal photo
                slides.append(Slide(self.photos[tag]['H'].pop()))

        for key,tag in enumerate(self.tags):
            while(len(self.photos[tag]['V']) > 1):    # handle vertical photos
                one = self.photos[tag]['V'].pop()
                two = self.photos[tag]['V'].pop()
                slides.append(Slide(one,two))

        return slides

    def solve_com(self):

        # choose first slide randomly
        if len(self.photos[self.tags[0]]['H']) > 0:
            last_photo = self.photos[self.tags[0]]['H'].pop()
        else:
            one = self.photos[self.tags[0]]['V'].pop()
            two = self.photos[self.tags[0]]['V'].pop()

        slides = [last_photo]

        for orient in ["V","H"]:
            for key,tag in enumerate(self.tags):
                print(orient,tag)
                while(True):
                    if len(slides) % 1000 == 0:
                        print(len(slides),self.count_photos)

                    if orient == "H":
                        if len(self.photos[tag][orient]) > 0:
                            # handle horizontal photo
                            best_score = -1
                            best_key = 0
                            for i in [-1,0,1]:
                                for key_np,next_photo in enumerate(self.photos[self.tags[key+i]][orient]):
                                    score = get_score(last_photo,next_photo)
                                    if score > best_score:
                                        best_score = score
                                        best_key = key_np
                                        best_tag = self.tags[key+i]

                            last_photo = self.photos[best_tag]['H'].pop(best_key)
                            slides.append(last_photo)
                        else:
                            break
                    else:
                        # handle vertical photos
                        if len(self.photos[tag]['V']) > 1:
                            best_score = -1

                            for i in range(1000):
                                key_one = randint(0,len(self.photos[tag]['V']) - 1)
                                key_two = randint(0,len(self.photos[tag]['V']) - 1)
                                tag_ids = set(self.photos[tag]['V'][key_one]['tags'])|set(self.photos[tag]['V'][key_two]['tags'])
                                slide = {'tags': tag,'id':(one['id'],two['id']),'tag_ids':tag_ids}
                                score = score(slide,last_photo)
                                if score > best_score:
                                    best_score = score
                                    best_keys = (key_one,key_two)
                                    best_slide = slide

                            for key_temp in sorted([key_one,key_two],reverse=True):
                                del self.photos[tag]['V'][key_temp]

                            slides.append(best_slide)
                        

                   
        return slides