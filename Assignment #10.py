import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

df = pd.read_csv('housePrices.csv')

y = df['SalePrice']

models = {
    "Model 1": ['Overall Qual', 'Total Liv Area', 'Garage Area'],
    "Model 2": ['Overall Cond', 'Total Bsmt SF', 'Full Bath'],
    "Model 3": ['Year Built', 'TotRms AbvGrd', 'Bedroom AbvGr']
}

for model_name, features in models.items():

    print("\n" + "="*40)
    print(f"{model_name}")
    print(f"Features: {features}")
    print("="*40)

    X = df[features]

    sumRmse = 0
    sumR2 = 0
    sumAdjR2 = 0

    run = 1

    for i in range(5, 35, 5):

        xTrain, xTest, yTrain, yTest = train_test_split(
            X, y, test_size=0.2, random_state=i
        )

        model = LinearRegression()
        model.fit(xTrain, yTrain)

        yPredict = model.predict(xTest)

        rmse = np.sqrt(mean_squared_error(yTest, yPredict))
        r2 = model.score(xTest, yTest)

        n = len(yTest)
        p = len(features)
        adjR2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))

        print(f"\nRun {run}")
        print(f"  RMSE     : {rmse:,.2f}")
        print(f"  R²       : {r2:.4f}")
        print(f"  Adj R²   : {adjR2:.4f}")

        sumRmse += rmse
        sumR2 += r2
        sumAdjR2 += adjR2

        run += 1

    print("\n" + "-"*40)
    print("AVERAGE RESULTS")
    print("-"*40)
    print(f"Mean RMSE   : {sumRmse / 6:,.2f}")
    print(f"Mean R²     : {sumR2 / 6:.4f}")
    print(f"Mean Adj R² : {sumAdjR2 / 6:.4f}")
