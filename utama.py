import os 
import alat
import master_exception
print(alat.area_square(9))
print(alat.perimeter_square(9))
print(alat.area_triangle(1,2))

try:
    score = int(input("Enter score: "))
    if score < 0 or score > 100:
        raise ValueError("score must be between 0-100")
except ValueError as e:
    print("input error: ", e)
else:
    print("score: ", score)
    print("description: ", master_exception(score))