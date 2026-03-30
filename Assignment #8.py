import csv
import pandas as pd

fatalitiesSeries = pd.Series(dtype=float)
accidentCountSeries = pd.Series(dtype=int)
fatalAccidentSeries = pd.Series(dtype=int)

with open("aviation.csv") as infile:
    reader = csv.reader(infile)
    reader.__next__()

    for rec in reader:
        make = rec[2]

        try:
            fatal = int(rec[4]) if rec[4] != '' else 0
        except:
            fatal = 0

        if make in fatalitiesSeries.keys():
            fatalitiesSeries[make] = fatalitiesSeries[make] + fatal
            accidentCountSeries[make] = accidentCountSeries[make] + 1

            if fatal > 0:
                fatalAccidentSeries[make] = fatalAccidentSeries[make] + 1

        else:
            fatalitiesSeries[make] = fatal
            accidentCountSeries[make] = 1
            fatalAccidentSeries[make] = 1 if fatal > 0 else 0


dict_data = {
    "Total Fatalities": fatalitiesSeries,
    "Total Accidents": accidentCountSeries,
    "Total Fatal Accidents": fatalAccidentSeries
}

dataframe = pd.DataFrame(dict_data)

print(dataframe.sort_index())
