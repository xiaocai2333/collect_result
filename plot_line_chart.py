import json
import numpy
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

result_file = "./results.txt"


def plot_line_chart(x, y, label, title):
    plt.plot(x, y, 'r--', label=label)
    # plt.scatter(x, y)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Speed')

    # plt.legend()
    plt.savefig('./' + title + '.jpg')
    plt.show()


if __name__ == "__main__":
    f = open(result_file, "r")
    line = f.readline()
    result_str = json.loads(line)
    for key in result_str:
        plot_line_chart(result_str[key]["InsertTime"], result_str[key]["Speed"], "insert", key)
