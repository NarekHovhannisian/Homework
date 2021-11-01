# Finding the Users Active Minutes
def findingUsersActiveMinutes(logs, k):
    unique = []
    for log in logs:
        if log not in unique:
            unique.append(log)

    d = {}
    answer = [0] * k
    for a, b in unique:
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1

    for key in d:
        answer[d[key] - 1] += 1

    return answer
