import math

class Methods():
    def MetropolisAcceptance(current_energy, neighbour_energy, Temp):
        return math.exp(-(neighbour_energy-current_energy)/Temp)

    def