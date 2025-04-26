from math import *
from scipy.stats import norm
class Models:
    def __init__(self):
        pass
    
    def getInterData(self, data, dCant):
        for x in data:
            if int(x[0][0]) <= dCant or dCant <= int(x[0][1]):
                return x


    def descModel(self, discList, dCant, originPrice):
        inter = self.getInterData(discList, dCant)
        discPrice = originPrice * (1-inter[1])

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
    
    def simpleModel(self, c, D, k, h, l, pe):
        result = []
        Q = 0
        e = 0
        costo = 0
        if pe == 0:
            Q = self.calcQ(D, k, h)
            result.append(f"Valor de Q: {Q}")
        else:
            Q = self.calcQFaltante(D, k, h, pe)
            e = self.calcE(D, k, h, pe)
            result.append(f"Valor de Q: {Q}")
            result.append(f"Valor de la Esperanza: {e}")

        T = Q / D
        result.append(f"Valor de T: {T}")
        if e == 0:
            costo = self.calcCosto(D, c, Q, h, k)
        else:
            costo = self.calcCostoFaltante(D, c, Q, h, k, e=e, pe=pe)
            
        result.append(f"Valor del Costo: {costo}")
        
        #print(f"Costo: {costo}")
        
        if l < T:
            R = D*l
        else:
            m = 0
            while(not(m*T < 0) and not(l - ((m+1)*T) > 0)): m+=1
            R = D * (l-m*T)


        result.append(f"Valor del Punto de Reorden(R): {R}")
        return [result, Q, D, c, h, k, e, pe]

    def calcQ(self, D, k, h):
        return sqrt((2*k*D)/h)

    def calcQFaltante(self, D, k, h, pe):
        return sqrt(((2*k*D)*(h+pe))/(h*pe))

    def calcE(self, D, k, h, pe):
        return sqrt((2*k*D*h) / (h+pe) * pe)

    def calcCosto(self, D, c, Q, h, k):
        return (c*D) + (k * (D/Q)) + ((1/2)*h*Q)

    def calcCostoFaltante(self, D, c, Q, h, k, pe, e):
        return (c*D) + (k * (D/Q)) + (h*(Q-e)**2 / 2*Q) + (pe**2 / 2*Q)
    
    def probModel(self, k, h, pA, u, dLab, des, pAPerdida):
        result = []
        E = self.calcEProb(u=u, dLab=dLab)
        Q = self.calcQProb(E=E, h=h, k=k)
        prob = self.calcProb(h=h, E=E, pA=pA, Q=Q)
        result.append(f"Valor de E: {E}")
        result.append(f"Valor de Q: {Q}")
        result.append(f"Prob: {prob}")
        if pAPerdida != 0:
            prob2 = self.calcProbPerdida(h=h, Q=Q, pAPerdida=pAPerdida, E=E)
            R1 = (abs(norm.ppf(prob)) * des) + u
            R2 = (abs(norm.ppf(prob2)) * des) + u
            # print(f"R1: {R1}")
            # print(f"R2: {R2}")
            result.append(f"Valor de R1: {R1}")
            result.append(f"Valor de R2: {R2}")
        else:
            R = (abs(norm.ppf(prob)) * des) + u
            # print(f"R: {R}")
            result.append(f"Valor de R: {R}")

        return [result]

    
    def calcEProb(self, dLab, u):
        return dLab * u
    
    def calcQProb(self, k, E, h):
        return sqrt(((2*k*E)/h))
    
    def calcProb(self, h,Q, pA, E):
        return (h*Q) / (pA * E)

    def calcProbPerdida(self, h, Q, pAPerdida, E):
        return (h*Q) / (h*Q+pAPerdida*E)
    
    def queuingModel(self, llegada, Servicio, n, tiempo, clientesN):
        landa = llegada
        u = Servicio
        result = []

        L = landa / (u - landa)
        result.append(f"Cantidad de Clientes en Cola: {L}")
        
        Lq = (landa**2) / (u*(u-landa))
        result.append(f"Cantidad de Clientes en Sistema: {Lq}")

        W = 1 / (u-landa)
        result.append(f"Tiempo Promedio en el Sistema: {W}")

        Wq = W - (1/u)
        result.append(f"Tiempo Promedio en Cola: {Wq}")
        
        p = landa / u
        probN = self.calcProbN(n, p)
        result.append(f"La Probabilidad de {n} o mas Clientes es: {round(probN*100, 2)}%")
        
        pN = (1-p)*(p**clientesN)
        result.append(f"La Probabilidad de {clientesN} Clientes es: {round(pN*100, 2)}%")

        tiempoEspera = exp(-1*(u-landa) * tiempo)
        result.append(f"La Probabilidad de Esperar {tiempo} es: {round(tiempoEspera*100, 2)}%")


        return [result, p]
    
    
    def probN(self, p, clientes):
        return (1-p)*(p**clientes)

    def calcProbN(self, n, p):
        resultP = []

        for i in range(n+1):
            resultP.append((1-p)*(p**i))

        return 1-sum(resultP)


