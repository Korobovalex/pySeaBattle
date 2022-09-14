# Тесты классов

from classes.Dot import Dot

# Dot test------------
dot1 = Dot(5, 3)
dot2 = Dot(2, 4)
dot3 = Dot(5, 3)

print(dot1 == dot2)
print(dot1 == dot3)

dots = [Dot(4, 4), Dot(1, 6), Dot(2, 4), Dot(5, 1)]
print(dot1 in dots)
print(dot2 in dots)
# / Dot test----------