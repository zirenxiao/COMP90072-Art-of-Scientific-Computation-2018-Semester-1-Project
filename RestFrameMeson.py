import numpy
SPEEDOFLIGHT = 2.9979e8 # unit m/s
MASSOFMUON = 105.7 # unit MeV/c2

class RestFrameMeson:
    # Apply Accept-Reject method on 2 uniform number
    # x1 and x2 from standard unifor distribution (0, 1),
    # return z1 and z2 for normal distribution with input
    # parameter (mean, sd), return None if the numbers are
    # rejected
    def acceptReject(self, x1, x2, mean, sd):
        u1 = 2*x1 - 1
        u2 = 2*x2 - 1
        d = u1*u1 + u2*u2
        if d <= 1:
            y1 = u1*numpy.sqrt(-2*numpy.log(d)/d)
            y2 = u2*numpy.sqrt(-2*numpy.log(d)/d)
            z1 = mean + sd*y1
            z2 = mean + sd*y2
            return z1, z2
        else:
            return None

    # Generate 2 mesons list, there is 86% chance
    # to be pion and 14% to be kaons
    def generateMesons(self, size, mean, sd):
        pions = []
        kaons = []
        count = 0
        while (count < size):
            uniform1 = numpy.random.uniform(0, 1)
            uniform2 = numpy.random.uniform(0, 1)
            result = self.acceptReject(uniform1, uniform2, mean, sd)
            if (result != None):
                prob = numpy.random.uniform(0, 1)
                if (prob <= 0.86):
                    pions.append(result[0])
                else:
                    kaons.append(result[1])
                count = count + 1
        return pions, kaons

    # Calculate decay time by using Inverse Transform
    # on lift time of meson, and randomly generate x
    # ranging from 0 to 1
    def inverseTransformMesonDecay(self, lifeTime):
        uniform = numpy.random.uniform(0, 1)
        result = -lifeTime*numpy.log10(uniform)
        return result

    # Calculate a meson distance travelled using
    # s = momentum / mass * decay time * c
    def singleMesonDistanceTravelled(self, p, m, time):
        result = (p / m) * time * SPEEDOFLIGHT
        return result

    # Group calculate distance of mesons travelled
    # Input
    #       lifeTime: lift time of the meson
    #       mass: mass of the meason
    #       arrays: array list of momentum of the meason
    # Return
    #       an array list containing elements in
    #       following format:
    #       [momentum of meson, distance of its travelling]
    def groupMesonDistanceTravelled(self, lifeTime, mass, arrays):
        results = []
        for item in arrays:
            time = self.inverseTransformMesonDecay(lifeTime)
            distance = self.singleMesonDistanceTravelled(item, mass, time)
            temp = []
            temp.append(item)
            temp.append(distance)
            results.append(temp)
        return results

    # Calculate momentum of a neutrino in rest frame
    def calculateNeutrinoMomentumRest(self, mass):
        result = (mass * mass - MASSOFMUON * MASSOFMUON) / (2 * mass)
        return result

    # Generate a valid and random angle
    def generateAngle(self):
        uniform = numpy.random.uniform(-1, 1)
        acos = numpy.arccos(uniform)
        return acos

    # Calculate longitudinal momentum, transverse momentum,
    # neutrino momentum and its angle in Rest frame
    def calculateRestMomentumMeson(self, mass):
        pv = self.calculateNeutrinoMomentumRest(mass)
        angle = self.generateAngle()
        pl = pv * numpy.cos(angle)
        pt = pv * numpy.sin(angle)
        return pl, pt, pv, angle
