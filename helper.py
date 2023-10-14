import json

class Helper:
    def taille(json_file):
        with open(json_file) as file:
            data = json.load(file)
            return sum(len(data[node]) for node in data)

    def ordre(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            return(len(data))