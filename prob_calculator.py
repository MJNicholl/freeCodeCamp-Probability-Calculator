import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():
            for i in range(v):
                self.contents.append(k)
        self.orignalContents = self.contents.copy()

    def draw(self, sample):
        balls_removed = []
        self.contents = self.orignalContents.copy()
        if sample > len(self.contents):
            balls_removed = self.contents
        else:
            for _ in range(sample):
                ball_removed_from_hat = random.choice(self.contents)
                balls_removed.append(ball_removed_from_hat)
                self.contents.remove(ball_removed_from_hat)
        
        return balls_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0

    # list the expected_balls as strings to later compare with samples
    expected_balls_list = []
    number_of_balls_expected = 0
    for k, v in expected_balls.items():
        number_of_balls_expected += v
        for i in range(v):
            expected_balls_list.append(k)

    if number_of_balls_expected <= num_balls_drawn:
        # count successfull experiments for probability
        expected_results_achieved = 0
        for _ in range(num_experiments):
            current_sample = hat.draw(num_balls_drawn)
            full_sets = 0

            for ball_color in set(expected_balls_list):
                if current_sample.count(ball_color) >= expected_balls_list.count(ball_color):
                    full_sets += 1

            sets_to_fill = len(set(expected_balls_list))
            if full_sets >= sets_to_fill:
                expected_results_achieved += 1

        if expected_results_achieved > 0:
            probability = expected_results_achieved / num_experiments
    
    return probability
