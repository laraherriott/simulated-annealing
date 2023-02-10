# Simulated Annealing

## Package: simulated_annealing

simulated-annealing is a package for conducting simulated annealing optimization in python.

Examples of the application of simulated annealing using this package can be found in the examples.ipynb file.

In brief, simulated annnealing can be run on your pre-defined objective function using the following two lines of code:

```python
simulate = SimulatedAnnealing(objective, bounds, temp_range, step_size, termination)
results, temperatures = simulate.SimulatedAnneal()
```

By default the package uses an exponential multiplicative cooling schedule, a gaussian method for choosing the neighbour, and the Metropolis acceptance criteria.
Further information on these various algorithm design features can be found in the file Background.md
