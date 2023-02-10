import numpy as np
from numpy.random import rand, uniform
from simulated_annealing import Methods

class SimulatedAnnealing():
    def __init__(self, model, bounds: list, temp_range: list, step_size:float, termination: dict, functions = [Methods.ExponentialMultiplicative, Methods.GaussianStep, Methods.MetropolisAcceptance]):
        self.initial_temp = temp_range[0]
        if temp_range[1] == None:
            self.final_temp = self.initial_temp/2
        else:
            self.final_temp = temp_range[1]
        self.step_size = step_size
        self.termination_style = list(termination.keys())[0]
        self.termination_value = list(termination.values())[0]
        self.k_max = None
        self.eval_max = None
        self.tol = None
        self.model = model
        self.bounds = bounds
        self.functions = functions

    def TerminationStyle(self):
        if self.termination_style == 'max_step':
            self.k_max = self.termination_value
        elif self.termination_style == 'max_eval':
            self.eval_max = self.termination_value
        elif self.termination_style == 'tolerance':
            self.tol = self.termination_value

    def DoTerminate(self):
        if self.k_max is not None:
            return self.count > self.k_max or self.T < 0
        elif self.eval_max is not None:
            return self.evaluations > self.eval_max or self.T < 0
        else:
            return self.T <= self.final_temp or self.model(self.s) == 0

    def ChooseInitial(self):
        return self.bounds[:, 0] + rand(len(self.bounds)) * (self.bounds[:, 1] - self.bounds[:, 0])

    def Cooling(self, timestep, current_temp, function):
        return function(self.initial_temp, timestep, current_temp)

    def ChooseNeighbour(self, s, function):
        """ This implementation takes random steps to the next point according to 
        a Gaussian distribution. An alternative function can be used specified.
        """
        return function(s, self.bounds, self.step_size)

    def AcceptingProbability(self, current_energy, neighbour_energy, Temp, function):
        if neighbour_energy < current_energy:
            return True
        else:
            rand = uniform()
            if function(current_energy, neighbour_energy, Temp) >= rand:
                return True
            else:
                return False

    def SimulatedAnneal(self):
        self.s = self.ChooseInitial()
        self.T = self.initial_temp
        self.k = 1
        self.count = 0
        self.evaluations = 0

        path = []
        path.append(self.s)
        temp_path = []
        temp_path.append(self.T)
        
        self.TerminationStyle()

        while not self.DoTerminate():
            # run 100 iterations before dropping the temperature
            for i in range(0, 100):
                s_new = self.ChooseNeighbour(self.s, self.functions[1])
                current_energy = self.model(self.s)
                neighbour_energy = self.model(s_new)
                if self.AcceptingProbability(current_energy, neighbour_energy, self.T, self.functions[2]):
                    path.append(s_new)
                    self.s = s_new
                    self.evaluations += 1
                else:
                    path.append(self.s)

                self.count += 1
            
            T_new = self.Cooling(self.k, self.T, self.functions[0])
            self.T = T_new
            temp_path.append(self.T)
            self.k += 1


        return path, temp_path


    