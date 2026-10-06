import json,asyncio

class Json_Repository:
    
    def read_file(self, file_path) -> list:

        with open(file_path, "r") as file:
            return json.load(file)
        
    async def read(self,file_path):
          return await asyncio.to_thread(self.read_file,file_path)
    
    async def append(self, file_path, data: dict) -> None:
        existing_data = await self.read(file_path)
        existing_data.append(data)
        await self.write(file_path,existing_data)

    def write_file(self, file_path, data: list) -> None:

        with open(file_path, "w") as file:
            json.dump(data , file , indent = 4)

    async def write(self,file_path,data : list):
        return await asyncio.to_thread(self.write_file,file_path,data)


