import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.drawn =[]
        self.contents= []
        for i ,v in colors.items():
            for j in range(v):
                self.contents.append(i)
        
    def draw(self, number):
        if number > len(self.contents) and number > len(self.drawn):
            return -1
        elif len(self.contents) < number and len(self.drawn) != 0:
            self.contents= copy.deepcopy(self.drawn)
            self.drawn= []
            single_draw= []
            for color in range(number):
                ball = random.choice(self.contents)
                single_draw.append(ball)
                self.contents.remove(ball)
                self.drawn.append(ball)
            return single_draw
        else:
            single_draw= []
            for color in range(number):
    
                ball = random.choice(self.contents)
                single_draw.append(ball)
                self.contents.remove(ball)
                self.drawn.append(ball)
        
            return single_draw

def experiment(hat, expected_balls , num_balls_drawn , num_experiments):
    
    stop = 0
    M= 0
    N = num_experiments
    while stop < N:
    
        single_draw= hat.draw(num_balls_drawn )
        if single_draw == -1 :
            M= num_experiments
            return M/N
        else:   
            ok = 0
            for k, v in expected_balls.items():
                if k in single_draw:
                    if single_draw.count(k) == v:
                        ok +=1
            if ok == 2:
                M += 1
        stop += 1
    return M/N


# if __name__ == "__main__":
    # hat1 = Hat(blue=4, red=2, green=6)
    # probability = experiment(hat=hat1,
    #                 expected_balls={"blue":2,"red":1},
    #                 num_balls_drawn=4,
    #                 num_experiments=7)
    # print(probability)

    # hat1 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
    # probability = experiment(hat=hat1,
    #                 expected_balls={"yellow":2,"blue":3,"test":1},
    #                 num_balls_drawn=20,
    #                 num_experiments=7)
    # print(probability)