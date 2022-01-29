def grade(gradeNum):
    if 90 <= gradeNum <= 100:
        return 'A'
    if 80 <= gradeNum <= 89:
        return 'B'
    if 70 <= gradeNum <= 79:
        return 'C'
    if 60 <= gradeNum <= 69:
        return 'D'
    if 0 <= gradeNum <= 59:
        return 'F'

gradeNum = int(input("What number grade did you get?: "))
print(grade(gradeNum))
