def advise(level):
    file = open("predictions.atom", "r")
    lines = file.readlines()
    file.close()
    advice = []
    # print(lines)
    if level <= 15:
        advice = lines[3]
    elif level <= 20:
        advice = lines[2]
    elif level <= 40:
        advice = lines[4]
    elif level <= 60:
        advice = lines[5]
    elif level <= 80:
        advice = lines[6]
    elif level >= 85:
        advice = lines[7]
    advice = str(lines[1])+str(level)+str(advice)
    print(advice)
    return advice
