#!/usr/bin/env python3
"""src/smoke_test.py — Load CSV and print the same output as the notebook."""

import pathlib
import pandas as pd


def main():
    data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"
    df = pd.read_csv(data_path)

    print("Shape:", df.shape)
    print(df.head())
    print(df.describe())


if __name__ == "__main__":
    main():