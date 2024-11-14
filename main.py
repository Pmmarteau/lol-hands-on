import pandas as pd


def load_csv(file_path):
    return pd.read_csv(file_path)


def main():
    data = load_csv("games.csv")
    print(data.head())


if __name__ == "__main__":
    main()
