import numpy
from RestFrameMeson import RestFrameMeson


LENGTHOFDECAYTUNNEL = 300 # unit m

restMeson = RestFrameMeson()

class LabFrameMeson:

    # Calculate beta in Lorentz trasformation
    def calculateBeta(self, pMeson, massMeson):
        result = pMeson / numpy.sqrt(pMeson*pMeson + massMeson*massMeson)
        return result

    # Calculate gamma in Lorentz trasformation
    def calculateGamma(self, beta):
        result = 1 / numpy.sqrt(1 - beta*beta)
        return result

    # Calculate longitudinal momentum, transverse momentum,
    # neutrino momentum and its angle in Lab frame
    def calculateLabMomentumMeson(self, pMesson, massMeson):
        beta = self.calculateBeta(pMesson, massMeson)
        gamma = self.calculateGamma(beta)
        pl, pt, pv, angle = restMeson.calculateRestMomentumMeson(massMeson)
        plLab = gamma * pl + beta*gamma*pv
        ptLab = pt
        energyLab = beta*gamma*pl + gamma*pv
        return plLab, ptLab, energyLab, angle

    # Group calculate momentum of mesons in lab frame
    # Input
    #       distances: distance result of meson in format
    #                  [momentum, distance]
    #       massMeson: mass of single meason
    # Return
    #       an array list containing elements in
    #       following format:
    #       [momentum of meson, longitudinal momentum in lab frame,
    #       transverse momentum in lab frame, energy in lab frame,
    #       angle in lab frame, distance travelled]
    def groupLabMomentumMeson(self, distances, massMeson, lifeTime):
        results = []
        for item in distances:
            if (item[0] <= LENGTHOFDECAYTUNNEL):
                plLab, ptLab, energyLab, angle = self.calculateLabMomentumMeson(item[0], massMeson)
                temp = []
                temp.append(item[0])
                temp.append(plLab)
                temp.append(ptLab)
                temp.append(energyLab)
                temp.append(angle)
                temp.append(item[1])
                results.append(temp)
        return results
