import pandas as pd


def load_colleagues(filepath: str) -> list[str]:
    Output= []

    with open(filepath, "r") as file:

        for line in file:
            Output.append(line.strip())

    return Output