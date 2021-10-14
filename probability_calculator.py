import copy
import random

class Hat:
    # expected arguments in form: object = Hat(colour1=quantity1,...)
    def __init__(self, **balls):
        contents = []
        for colour in balls:
            for q in range(balls[colour]):
                contents.append(colour)
        self.contents = contents

    def draw(self, n_draw):
        if n_draw > len(self.contents):
            return self.contents
        else:
            draw_sample = []
            for n in range(n_draw):
                rand_draw = random.randrange(len(self.contents) )
                draw_sample.append(self.contents[rand_draw] )
                del self.contents[rand_draw]
            return draw_sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for exp_num in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        draw_sample = exp_hat.draw(num_balls_drawn)

        for colour in expected_balls.keys():
            if draw_sample.count(colour) < expected_balls[colour]:
                success = False
                break
            else:
                success = True
        if success:
            success_count += 1
    return success_count/num_experiments


# tests
hat1 = Hat(red = 2, blue = 3, green = 2, yellow = 2, black = 1)
# print(hat1.contents)
# print(hat1.draw(3) )
# print(hat1.contents)
print(experiment(hat1, {"blue":2, "black":1}, 5, 20000) )
