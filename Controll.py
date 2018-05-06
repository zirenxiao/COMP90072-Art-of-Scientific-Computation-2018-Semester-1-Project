import numpy
from RestFrameMeson import RestFrameMeson
from LabFrameMeson import LabFrameMeson

MASSOFPIONS = 139.6 # unit MeV/c2
MASSOFKAONS = 493.7 # unit MeV/c2
LIFETIMEOFPIONS = 2.608e-8 # unit s
LIFETIMEOFKAONS = 1.237e-8 # unit s

restMeson = RestFrameMeson()
labMeson = LabFrameMeson()

class Controll:
    def pionsDistanceTravelled(self, pions):
        return restMeson.groupMesonDistanceTravelled(LIFETIMEOFPIONS, MASSOFPIONS, pions)
    def kaonsDistanceTravelled(self, kaons):
        return restMeson.groupMesonDistanceTravelled(LIFETIMEOFKAONS, MASSOFKAONS, kaons)
    def getDistance(self, distances):
        result = []
        for item in distances:
            result.append(item[1])
        return result
    def getMomentum(self, distances):
        result = []
        for item in distances:
            result.append(item[0])
        return result

    def pionsLabMomentum(self, distances):
        return labMeson.groupLabMomentumMeson(distances, MASSOFPIONS, LIFETIMEOFPIONS)
    def kaonsLabMomentum(self, distances):
        return labMeson.groupLabMomentumMeson(distances, MASSOFKAONS, LIFETIMEOFKAONS)
    def getLongitudinals(self, results):
        r = []
        for item in results:
            r.append(item[1])
        return r
    def getTransverse(self, results):
        r = []
        for item in results:
            r.append(item[2])
        return r
