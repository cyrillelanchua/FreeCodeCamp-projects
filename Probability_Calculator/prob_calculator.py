import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for item in kwargs.keys():
            while(kwargs[item] != 0):
                self.contents.append(item)
                kwargs[item] -= 1
        # for the repeaded use of draw_modified function
        self.contents_copy = self.contents.copy()

    def draw(self, count_ball): #alters self.contents   
        if count_ball > len(self.contents):
            return self.contents
        drawn_balls = []
        for i in range(count_ball):
            index = random.randint(0, len(self.contents)-1)
            drawn_balls.append(self.contents[index])
            self.contents.pop(index)
        return drawn_balls

    def draw_modified(self, count_ball): #does not alter any self variable
        if count_ball > len(self.contents_copy):
            return self.contents_copy
        copy_content = self.contents_copy.copy()
        drawn_balls = []
        for i in range(count_ball):
            index = random.randint(0, len(copy_content)-1)
            drawn_balls.append(copy_content[index])
            copy_content.pop(index)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments=0):
    M = 0
    for i in range(num_experiments):
        inside = True
        drawn_balls = hat.draw_modified(num_balls_drawn)
        dic_balls = {}
        for ball in drawn_balls:
            dic_balls[ball] = dic_balls.get(ball,0) +1
        for key in expected_balls.keys():
            inside = key in dic_balls and expected_balls[key] <= dic_balls[key]
            if inside == False:
                break
        if inside == True:
            M+=1
    return M/num_experiments

    
prob_calculator = Hat(yellow=3, blue=2, green=6)
print(prob_calculator.contents)
print(prob_calculator.draw(2))
print(prob_calculator.contents)
experiment(prob_calculator,expected_balls={"yellow":1, "blue":1, "green":1}, num_balls_drawn=3,num_experiments=5)
hat = Hat(blue=3,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=11, num_experiments=1000))
