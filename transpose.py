import cv2
import sys


def cv_transpose(in_filename, out_filename):
    input_image = cv2.imread(in_filename)
    output_image = cv2.transpose(input_image)
    cv2.imwrite(out_filename, output_image)


""" Other implementation
def transpose(filename):
    input_image = cv2.imread(filename)
    output_image = cv2.flip(cv2.rotate(input_image, cv2.cv2.ROTATE_90_CLOCKWISE), 1)
    cv2.imshow("Result2", output_image)"""

cv_transpose(sys.argv[1], sys.argv[2])
