import json

class Stat:
    def __init__(self, name):
        self.name = name
        with open('docs/functions/stat/config.json', 'r+') as statJson:
            statdata = json.load(statJson)
            newtask = {
                "name": self.name,
                "xp": 0
            }
            statdata["stats"].append(newtask)
            statJson.seek(0)
            json.dump(statdata, statJson, indent=4)

    def add_xp(self, statname, amt):
        with open('docs/functions/stat/config.json', 'r+') as statJson:
            statdata = json.load(statJson)
            for item in statdata['stats']:
                if item["name"] == statname:
                    item["xp"] += amt
                    statJson.seek(0)
                    json.dump(statdata, statJson, indent=4)