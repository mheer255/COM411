import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...", end="")

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for line in csv_reader:
            records.append(line)

    print("Done!")


def run():
    load_data("titanic.csv")


num_records = len(records)
print(f"Successfully loaded {num_records} records.")

if __name__ == "__main__":
    run()
