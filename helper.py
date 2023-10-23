import json

class Helper:
    def taille(data):
        return sum(len(data[node]) for node in data)

    def ordre(data):
        return(len(data))