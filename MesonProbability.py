import numpy

BEHINDMESONS = 700 # unit m
DETECTORRADIUS = 1.5 # unit m

class MesonProbability:
    def calculateRadialPosition(self, pt, angle, s):
        result = numpy.abs((s - BEHINDMESONS) * numpy.sin(angle))
        return result
    def calculatePercentHitDetector(self, labResult):
        count = 0
        for item in labResult:
            pt = item[2]
            if pt < 0:
                continue
            angle = item[4]
            distance = item[5]
            radialPosition = self.calculateRadialPosition(pt, angle, distance)
            if (radialPosition <= DETECTORRADIUS):
                count = count + 1
        return count
