import numpy as np
import random
import math

from Methods import MetropolisAcceptance

class SimulatedAnnealing():
    def __init__():
        pass

    def ChooseInitial():
        pass

    def Cooling(Temp, timestep, function=):
        pass

    def ChooseNeighbour():
        pass

    def AcceptingProbability(current_energy, neighbour_energy, Temp, function=MetropolicAcceptance):
        if neighbour_energy < current_energy:
            return True
        else:
            rand = random.random()
            if function(current_energy, neighbour_energy, Temp) >= rand:
                return True
            else:
                return False

    def SimulatedAnneal():
        pass

    