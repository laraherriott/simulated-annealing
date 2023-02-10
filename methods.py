import math
from numpy.random import randn

class Methods():
    def MetropolisAcceptance(current_energy, neighbour_energy, Temp):
        return math.exp(-(neighbour_energy-current_energy)/Temp)

    def ExponentialMultiplicative(initial_temp, timestep, current_temp):
        # Cooling schedule as proposed by Kirkpatrick, Gelatt and Vecchi (1983)
        return initial_temp*(0.95**timestep)

    def LinearDecrease(initial_temp, timestep, current_temp):
        return current_temp - 0.01 

    def GaussianStep(initial_point, bounds, step_size):
        return initial_point + randn(len(bounds)) * step_size