import pandas as pd
import numpy as np


def prepare_dataset():
    # Ouverture des fichiers train et test avec pandas
    train = pd.read_csv("train.csv", sep=",", index_col=[0])
    test = pd.read_csv("test.csv", sep=",", index_col=[0])

    # Concatenation de train et test
    data = pd.concat([test, train])

    # Mélange les entrées aléatoirement
    data = data.sample(frac=1).reset_index(drop=True)

    # Création d'une colonne date avec des valeurs aléatoires du 1/1/2018 au 1/1/2023
    data["date"] = np.random.choice(pd.date_range('2018-01-01', '2023-01-01'), len(data))

    return data


if __name__ == '__main__':
    data = prepare_dataset()

    # Sauvegarde du fichier data au format .csv
    data.to_csv("data.csv")
