def pascal(number) :
    if number == 0 :return [1]
    else :
        line = [1]
        previousLine = pascal(number - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i+1])
            line += [1]
        return line


number = 3
print(pascal(number))