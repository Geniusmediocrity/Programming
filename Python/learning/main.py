import cv2

imgCode = cv2.imread("code.png")
LANG = {(0, 0, 0): " ",
        (127, 127, 127): "\"",
        (136, 0, 21): ",",
        (237, 28, 36): "(",
        (255, 127, 39): ")",
        (255, 242, 0): "print",
        (34, 177, 76): "input"}

CODE = ""
for y in range(len(imgCode)):
    for x in range(0, len(imgCode[0])):
        if (imgCode[y, x] != (255, 255, 255)).any():
            CODE += LANG[(int(imgCode[y, x, 2]), int(imgCode[y, x, 1]), int(imgCode[y, x, 0]))]

print(CODE)
exec(CODE)