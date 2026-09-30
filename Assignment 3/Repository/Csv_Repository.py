import csv


class Csv_Repository:
    def read(self, file_path) -> list:

        with open(file_path, "r", newline="") as file:
            return list(csv.DictReader(file))
    
    def append(self, file_path, fields: list, data: dict) -> None:

        with open(file_path, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow(data)

    def write(self, file_path, fields: list, data: list) -> None:

        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

            