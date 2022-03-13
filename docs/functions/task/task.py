import json


from stat import *


class Task:
    def __init__(self, name, statincrease):
        self.name = name
        self.statincrease = statincrease

    def create_task(self):
        with open('docs/functions/task/config.json', 'r+') as taskJson:
            taskdata = json.load(taskJson)
            newtask = {
                "name": self.name,
                "stat increase": self.statincrease
            }
            taskdata["tasks"].append(newtask)
            taskJson.seek(0)
            json.dump(taskdata, taskJson, indent=4)

    def check_level(self):
        pass