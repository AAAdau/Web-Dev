if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Sort the students list based on their scores
    students.sort(key=lambda x: x[1])
    
    # Find the second lowest grade
    second_lowest_grade = sorted(list(set([student[1] for student in students])))[1]
    
    # Find all students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    
    # Print the names of second lowest grade students in alphabetical order
    for name in sorted(second_lowest_students):
        print(name)
