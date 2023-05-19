import os
import sys
import cv2

input_dir = "D:/Desktop/Temp/test"
output_dir = "D:/Desktop/Temp/test1"
img_dir = "D:/Desktop/DeepSea/Dataset/_LABELED-FISHES-IN-THE-WILD/Training_and_validation/Positive_fish"

classes = ["fish"]
temp = ""
box = []

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        with open(input_dir + '/' + filename) as f:#读文件到f
            content = f.readlines()  #读取f里的文件
        content = [x.strip() for x in content]  #去空白符和制表符
        for line in content:
            line = line.split(' ')
            img = cv2.imread(img_dir + '/' + line[0])
            height, width, channels = img.shape  # img[0]是高即cols，网上博客写错了误导人
            class_index = int(line[1]) - 1
            output = []
            j = 2
            if temp != line[0]:
                box = ''.join(box)
                with open(output_dir + '/' + temp[0:-4] + ".txt", 'w') as f:
                    f.write(box)
                box = []
            while(j+4<=len(line)):
                x, y, w, h = float(line[j]), float(line[j+1]), float(line[j+2]), float(line[j+3])
                x_mid = (x + w / 2) / width
                y_mid = (y + h / 2) / height
                width_norm = w / width
                height_norm = h / height
                output.append('{} {:.6f} {:.6f} {:.6f} {:.6f}'.format(class_index, x_mid, y_mid, width_norm, height_norm))
                output.append('\n')
                box.append('{} {:.6f} {:.6f} {:.6f} {:.6f}'.format(class_index, x_mid, y_mid, width_norm, height_norm))
                box.append('\n')
                j = j+4
            temp = line[0]
            output = ''.join(output)
            with open(output_dir + '/' + line[0][0:-4]+".txt", 'w') as f:
                    f.write(output)