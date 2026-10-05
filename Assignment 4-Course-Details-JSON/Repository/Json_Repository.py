import json


class Json_Repository:
    
    def read(self, file_path) -> list:

        with open(file_path, "r") as file:
            return json.load(file)
    
    def append(self, file_path, data: dict) -> None:

        existing_data = self.read(file_path)
        existing_data.append(data)
        with open(file_path, "w") as file:
            json.dump(existing_data, file, indent=4)

    def write(self, file_path, data: list) -> None:

        with open(file_path, "w") as file:
            json.dump(data , file , indent = 4)

            