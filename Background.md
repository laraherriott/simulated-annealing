## Background

Simulated annealing is an optimization technique designed to approximate the global optimum of a function. The algorithm takes its name from the process of annealing in metallury, in which by heating the metal to a high temperature initially and then slowly cooling it, the properties of the metal can be optimized to make the metal more workable.

The analogy between the algorithm and physical heat treatment applies to the concepts of starting at a 'high temperature', and to the 'slow cooling', and it is these features which allow the simulated annnealing algorithm to find the global optimum.

Compared to local optimization algorithms, such as hill climbing, simulated annealing is able to search for the global optima by accepting moves which increase the value of the function. The probability of accepting these worse solutions is known as the 'temperature' and, as in annealing of metals, the temperature is intially high and is gradually reduced as the number of iterations of the algorithm increases.

The initially high probability of accepting a worse solution allows the algorithm to effectively search the solution space in the early iterations. Then, as the tendency to accept better solutions only increases, the search tends towards and optimal solution, which has a high likelihood of being the global optimum as a result of the initial search.

The pseudocode for simulated annealing is given below. $E()$ is the objective function, $P()$ is the probability of accepting an increase, $ChooseNeighbour()$ defines the method for choosing the next point, $CoolTemperature()$ defines the cooling schedule, and $s$ and $s_{new}$ are the current and proposed next points, respectively.

```
SET s = s0
SET temperature = initial temperature
WHILE not termination condition
  FOR k = 0...kmax
    snew = ChooseNeighbour()
    temperature = CoolTemperature()
    IF E(snew) < E(s)
      s = snew
    ELSE
      IF P(E(s), E(snew), temperature) >= random(0, 1)
        s = snew
```

As can be seen from this pseudocode, there are a number of different features of the algorithm which need to be defined. Unfortunately, there is no one-size-fits-all approach for determining these various methods. However, some are used more commonly. Though some are used as defaults in this implementation, others can be specified by the used.

**Probability Function**

The most commonly used probability function is the metropolis acceptance criterion. Here, a worse solutionn is accepted with $P(E(s), E(snew), temperature) = e^{(-E(s_{new})-E(S))/temperature}$.

**Neighbour Choice**

A wide range of possible options are available for choosing the neighbour. In this implementation, the neighbour is chosen from a Gaussian distribution with $mean = current point$ and $s.d. = step size$, where the step size is defined by the used.

**Cooling Schedule**

Many cooling schedules are possible, ranging from linear to exponential, and also including those which scale temperature according to the difference between the current solution and the objective. In simulated annealing two options are implemented.

First, an exponential multiplicative cooling:
$T_{new} = T_{initial} 0.95^{k}$
where k is the current cycle.

Second, a linear cooling:
$T_{new} = T_{current} - 0.01$

Another factor to consider is how many iterations of the algorithm are conducted before the temperature is dropped. In this implementation this number is set at 100.

**Termination**
There are three termination options available in this implementation which can be determined by setting the termination and temp_range parameters accordingly.
1. 'max_step': A maximum number of total iterations.
2. 'max_eval': A maximum number of evaluations, meaning a maximum number of steps to new points.
3. Temperature: Terminate when the temperature reaches the minimum defined value. 
