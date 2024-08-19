def solution(participant, completion):
    race = {}
    for name in participant:
        if race.get(name) == None:
            race[name] = 1
        else:
            race[name] += 1

    for name in completion:
        race[name] -= 1

    for name in race.keys():
        if race[name] != 0:
            return name

    return ''

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))