from commands import *

# Just a sample
DATA = [{
    'neutralization': 'SUBINDUSTRY',
    'decay': 10,
    'truncation': 0.1,
    'delay': 1,
    'universe': 'TOP3000',
    'region': 'USA',
    'code': 'open + close'
}]

def functD1(alphas):
    res = []
    universe = ["TOP3000", "TOP1000"]
    for alpha in alphas:
        for universes in universe:
            # Simulate the alpha
            simulationSubIndustry = {
                'neutralization': 'SUBINDUSTRY',
                'decay': 10,
                'truncation': 0.05,
                'delay': 1,
                'universe': universes,
                'region': 'USA',
                'code': alpha
            }
            # Simulate the alpha
            simulation = {
                'neutralization': 'NONE',
                'decay': 10,
                'truncation': 0.05,
                'delay': 1,
                'universe': universes,
                'region': 'USA',
                'code': alpha
            }
            res.append(simulationSubIndustry)
            res.append(simulation)
    return res

def functD11K(alphas):
    res = []
    universe = ["TOP1000"]
    for alpha in alphas:
        for universes in universe:
            # Simulate the alpha
            simulationSubIndustry = {
                'neutralization': 'SUBINDUSTRY',
                'decay': 10,
                'truncation': 0.05,
                'delay': 1,
                'universe': universes,
                'region': 'USA',
                'code': alpha
            }
            # Simulate the alpha
            simulation = {
                'neutralization': 'NONE',
                'decay': 10,
                'truncation': 0.05,
                'delay': 1,
                'universe': universes,
                'region': 'USA',
                'code': alpha
            }
            res.append(simulationSubIndustry)
            res.append(simulation)
    return res

def functD0(alphas):
    res = []
    universe = ["TOP3000", "TOP500", "TOP1000"]
    for alpha in alphas:
        for universes in universe:
            # Simulate the alpha
            simulationSubIndustry = {
                'neutralization': 'SUBINDUSTRY',
                'decay': 10,
                'truncation': 0.1,
                'delay': 0,
                'universe': universes,
                'region': 'USA',
                'code': alpha
            }
            # Simulate the alpha
            simulation = {
                'neutralization': 'NONE',
                'decay': 10,
                'truncation': 0.1,
                'delay': 0,
                'universe': universes,
                'region': 'USA',
                'code': alpha
            }
            res.append(simulationSubIndustry)
            res.append(simulation)
    return res
