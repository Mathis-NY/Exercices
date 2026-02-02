import csv
import pandas as pd

populationDict = {}
countyCountDict = {}

with open("population.csv") as infile:
    reader = csv.reader(infile)
    reader.__next__()

    for rec in reader:
        state = rec[0]
        population = int(rec[2])

        if state in populationDict.keys():
            populationCount = populationDict[state]
            populationCount = populationCount + population
            countyCount = countyCountDict[state]
            countyCount = countyCount + 1
        else:
            populationCount = population
            countyCount = 1

        populationDict[state] = populationCount
        countyCountDict[state] = countyCount

populationSeries = pd.Series(populationDict)
countyCountSeries = pd.Series(countyCountDict)

averagePopulationPerState = populationSeries / countyCountSeries
averagePopulationPerState = averagePopulationPerState.sort_values()

print(round(averagePopulationPerState).astype(int))
