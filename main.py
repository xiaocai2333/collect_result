import datetime
import json
import os

log_path = "./results_log"
result_file = "./results.txt"
results = {}


def define_result(file, role):
    f = open(log_path + "/" + file, 'r')
    line = json.loads(f.readline())
    for key in line:
        results[role][key] = []


def collect_result(file, role):
    f = open(log_path + "/" + file, 'r')
    for line in f.readlines():
        line_str = json.loads(line)
        for key in line_str:
            if key == "InsertTime":
                time = line_str[key].replace(line_str[key].split('T')[0] + "T", "").replace('.' + line_str[key].split('.')[-1], "")
                results[role][key].append(time)
                continue
            results[role][key].append(line_str[key])


if __name__ == "__main__":
    files = os.listdir(log_path)
    for file in files:
        role = file.replace(".txt", "")
        results[role] = {}
        if not os.path.isdir(file):
            define_result(file, role)
            collect_result(file, role)

    print(results)
    with open(result_file, "w+") as f:
        f.write(json.dumps(results))
