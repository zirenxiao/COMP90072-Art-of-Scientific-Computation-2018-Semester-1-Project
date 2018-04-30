import numpy
SPEEDOFOBSERVER = 1
MASSOFELECTRON = 9.11e-31
class Calculation:
    def calculateKineticEnergy(self, p, m):
        c = SPEEDOFOBSERVER
        return (numpy.sqrt(pow(p*c, 2)+pow(c, 4)*m*m) - m*c*c)
    def getGroupKineticEnergy(self, p):
        results = []
        for momentum in p:
            results.append(self.calculateKineticEnergy(momentum, MASSOFELECTRON))
        return results
    def positionOfPeak(self, xs):
        max = 0
        maxPosition = 0
        current = 0
        for item in xs:
            if item > max:
                max = item
                maxPosition = current
            current = current + 1
        return maxPosition
