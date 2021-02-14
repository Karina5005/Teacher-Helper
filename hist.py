import cv2
import sys


def hist(filename):
    input_image = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
    res = {}
    for i in range(0, input_image.shape[0]):
        for j in range(0, input_image.shape[1]):
            if res.get(tuple(input_image[i, j])):
                res[tuple(input_image[i, j])] += 1
            else:
                res[tuple(input_image[i, j])] = 1
    for item in sorted(res.items(), key=lambda x: x[1], reverse=True):
        print(str(item[0])[1:-1], item[1], sep=': ')


hist(sys.argv[1])
