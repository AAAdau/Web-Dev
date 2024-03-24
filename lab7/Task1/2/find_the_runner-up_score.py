if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Convert map object to list and sort it in descending order
    scores = sorted(list(arr), reverse=True)
    
    # Find the index of the second highest score
    runner_up_index = scores.index(max(scores)) - 1
    
    # Print the runner-up score
    print(scores[runner_up_index])
