from Slide import *
from Score import *
from random import *


class Solver:
    def __init__(self,photos,tags,file):
        self.photos = photos
        self.tags = sorted(tags.keys())
        self.count_photos = 0
        self.file = file
        print("Tags with counts")
        for (key,val) in sorted(tags.items(),key=lambda x: x[1]['H'] + x[1]['V']):
            print(key,val)
            self.count_photos += val['H'] + val['V']
        print("Tags (sorted)",self.tags)


    def random_slide(self):
        # choose first slide randomly
        if len(self.photos[self.tags[0]]['H']) > 0:
            key = randint(0,len(self.photos[self.tags[0]]['H']) - 1)
            slide = Slide(self.photos[self.tags[0]]['H'].pop(key))
        else:
            population = range(len(self.photos[self.tags[0]]['V']))
            key_one,key_two = sample(population,2)
            slide = Slide(self.photos[self.tags[0]]['V'][key_one],self.photos[self.tags[0]]['V'][key_two])
            for key_temp in sorted([key_one,key_two],reverse=True):
                del self.photos[self.tags[0]]['V'][key_temp]
        print("Randomly choses start slide")
        print(slide)
        return slide

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

    def solve_complex(self):
        slide = self.random_slide()
        slides = [slide]
        found_early = 0
        found = 0

        for key,tag in enumerate(self.tags):
            found_early = 0
            found = 0
            while(len(self.photos[tag]['H']) > 0):
                best = {'key':0,'score':-1,'tag':tag}
                # add more i here to optimise
                for i in [0]:
                    if i+key < len(self.tags) and i+key > 0:
                        for key_np,slide in enumerate(self.photos[self.tags[key+i]]["H"]):
                            score = get_score(slide,slides[-1])
                            if score > best['score']:
                                best = {'key':key_np,'score':score,'tag':self.tags[key+i]}
                                # make window smaller to optimise
                                if score >= int(tag/2):
                                    found_early += 1
                                    break
                        else:
                            continue
                        break

                found += 1
                if found % 1000 == 0:
                    print("File {} Orient {} Tag {} Slides {} Found {} Early {} Remaining {}".format(self.file,"H",tag,len(slides),found,found_early,len(self.photos[tag]['H'])))
                slides.append(Slide(self.photos[best['tag']]['H'].pop(best['key'])))

        print("H finished for",self.file)

        for key,tag in enumerate(self.tags):
            found_early = 0
            found = 0
            while(len(self.photos[tag]['V']) > 1):    # handle vertical photos
                one = self.photos[tag]['V'].pop()
                two = self.photos[tag]['V'].pop()
                slides.append(Slide(one,two))
                found += 1
                if found % 1000 == 0:
                    print("File {} Orient {} Tag {} Slides {} Found {} Early {} Remaining {}".format(self.file,"V",tag,len(slides),found,found_early,len(self.photos[tag]['H'])))
                
        print("V finished for",self.file)

        print("------------------------------")
        print("Finished",self.file)
        print("------------------------------")

        return slides