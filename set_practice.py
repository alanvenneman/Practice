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
mylist = []
modulus = []
for i in weights:
    remainder = desired_weight//i
    mylist.append(remainder)
for i in weights:
    number = desired_weight % i
    modulus.append(number)

print(mylist)
print(modulus)

