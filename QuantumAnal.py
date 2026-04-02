def quantum_analyze(data):
    result = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data)):
            temp.append(data[i])
        result.append(sum(temp) / len(temp)%2)
    return result
