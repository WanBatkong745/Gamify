import json


from stat import *
from utils import *


class Task:
    def __init__(self, name, *stats):
        self.name = name
        self.stats = stats

        with open('docs/functions/task/config.json', 'r+') as taskJson:
            taskdata = json.load(taskJson)
            for stat in stats:
                values = stat.split(' + ')
                statname = values[0]
                statincrease = values[1]
                stats = {
                    "stat name": statname,
                    "stat increase": statincrease,
                }

            newtask = {
                "name": self.name,
                "stats": [stats]
            }
            
            taskdata["tasks"].append(newtask)
            taskJson.seek(0)
            json.dump(taskdata, taskJson, indent=4)



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

    '''def get_stats(self):
        stats_affected = []
        typing_print(f"Please enter the stats you would like to be affected by completing the task")
        for i in range(0, self.numberofstats):
            s = typing_input(": ")
            stats_affected.append(s)
        return stats_affected.value()'''

    def check_level(self):
        pass