

class Models:
    def __init__(self):
        pass

    def ABC(self, data):
        list(map(lambda x: x.append(x[1]*x[2]), data))
        data.sort(key=lambda x: x[3], reverse=True)
        totalSum = sum([x[3] for x in data])
        typeA = totalSum * 0.8
        typeC = totalSum * 0.05
        auxA = 0
        auxC = 0
        
        a = []
        bc = []
        popList = []
        for i, x in enumerate(data):
            if x[3] + auxA <= typeA:
                a.append([f"N-{x[0]}", x[1], x[2], x[3], "A"])
                auxA += x[3]
                popList.append(i)
            else:
                break
        [data.pop(0) for i in popList]

        
        for x in data[::-1]:
            if x[3] + auxC <= typeC:
                auxC += x[3]
                bc.append([f"N-{x[0]}", x[1], x[2], x[3], "C"])
            else:
                bc.append([f"N-{x[0]}", x[1], x[2], x[3], "B"])


        [a.append(x) for x in bc[::-1]]
        return a