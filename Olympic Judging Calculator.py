
def olympicJudging(numOfJudges):

    # in java, one would just make an array of size "numOfJudges"
    scores = []

    for i in range(0,numOfJudges):

        score = float(input('\nEnter a score: '))
        while score < 0 or score > 10:
            print('\nInvalid entry')
            score = float(input('\nEnter a score: '))
        scores.append(score)

    print(scores)

    high = max(scores)
    low = min(scores)
    
    scores.remove(high)
    scores.remove(low)

    average = sum(scores) / len(scores)
    print('Average: ',average)

olympicJudging(2)
            
