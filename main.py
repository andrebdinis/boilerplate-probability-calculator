# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

# PERSONAL NOTE: random.seed(95) is defined with a constant number so that freeCodeCamp can run their tests on a same generated sequence (if you pass a constant number as a random.seed() argument, the generated sequence will always be the same).
prob_calculator.random.seed(95)


# Example test
hat = prob_calculator.Hat(blue=4, red=2, green=6)
expected_balls = {"blue": 2, "red": 1}
num_balls_drawn = 4
num_experiments = 3000
probability = prob_calculator.experiment(hat=hat, expected_balls=expected_balls, num_balls_drawn=num_balls_drawn, num_experiments=num_experiments)
print("Hat Contents:\n", hat.contents)
print("Expected Balls:", expected_balls)
print("Number of Balls Drawn:", num_balls_drawn)
print("Number of Experiments:", num_experiments)
formattedProbability = str(round(probability * 100, 1))
print("Probability: " + formattedProbability + "%")


# Run unit tests automatically
main(module='test_module', exit=False)
