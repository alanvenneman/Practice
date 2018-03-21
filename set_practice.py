"""
Given a set, weights, and an integer desired_weight, remove the element of the set that is closest to desired_weight
(the closest element can be less than, equal to OR GREATER THAN desired_weight), and associate it with the variable
actual_weight. For example, if weights is (12, 19, 6, 14, 22, 7) and desired_weight is 18, then the resulting set
would be (12, 6, 14, 22, 7) and actual_weight would be 19. If there is a tie, the element LESS THAN desired_weight is
to be chosen. Thus if the set is (2, 4, 6, 8, 10) and desired_weight is 7, the value chosen would be 6, not 8. Assume
there is at least one value in the set.
"""

weights = {12, 19, 6, 14, 22, 7}
desired_weight = 18
# create a list of absolute values
abs_values = []
smallest_values = [] # How do I put the smallest values from abs_values here?
for i in weights:
    number = abs(desired_weight - i)
    abs_values.append(number)
# find the smallest absolute value
smallest = min(abs_values)
# count minimum values
if abs_values.count(min(abs_values)) > 1:
    print("There is more than one close to desired weight. Therefore, we shall choose the smallest number.")
# create dictionary to link weights to absolute values
weights_list = list(weights)
weights_values = dict(zip(weights_list, abs_values))
for k, v in weights_values.items():
    if v == smallest:
        smallest_values.append(k)
print(min(smallest_values))
