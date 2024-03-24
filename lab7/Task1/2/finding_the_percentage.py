if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Calculate the average score for the query_name
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # Print the average score with 2 decimal places
    print("{:.2f}".format(average_score))
