def MassVote(n, votes):
    percentage = []
    for i in range(n):
        percentage.append(votes[i]/sum(votes))

    winner = max(percentage)
    if percentage.count(winner) > 1:
        return 'no winner'
    else:
        k = percentage.index(winner) + 1
        if winner > 0.5:
            return 'majority winner ' + str(k)
        else:
            return 'minority winner ' + str(k)
