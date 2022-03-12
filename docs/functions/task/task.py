import json

class Task:
    def __init__(self, name, *statincrease):
        self.name = name
        self.statincrease = statincrease


    def create_task(self):
        with open('docs/functions/task/config.json', 'r+') as configJson:
            taskdata = json.load(configJson)
            newtask = {
                "name": self.name,
                "stat increase": self.statincrease
            }
            taskdata["tasks"].append(newtask)
            configJson.seek(0)
            json.dump(taskdata, configJson, indent=4)
