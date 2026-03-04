import pathlib
import pandas as pd

def main() -> None:
    data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"
    df = pd.read_csv(data_path)

    print("Shape:", df.shape)
    print(df.head())
    print(df.describe())

if __name__ == "__main__":
    main()
