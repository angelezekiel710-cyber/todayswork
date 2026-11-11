 #STUDENT INFORMATION
def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3)/ 3

def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

average = calculate_average(80, 70, 90)
grade = get_grade(average)
print("average", average)
print("grade", grade)


          #UNIT TESTING
def add(a,b):
    return a + b
assert add(21,45) == 66
assert add(2,4) == 7
print("all test passed.")
              


    