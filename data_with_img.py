
import os
import shutil

input_dir = "D:/Desktop/Temp/test_img/test.txt"
input_img_dir = "D:/Desktop/DeepSea/Dataset/_LABELED-FISHES-IN-THE-WILD/Training_and_validation/Positive_fish"
output_dir = "D:/Desktop/Temp/test_img"


with open(input_dir, 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for line in content:
    line = line.split(' ')
    for filename in os.listdir(input_img_dir):
        if filename in line[0]:
            shutil.move(input_img_dir+'/' + filename, output_dir+'/' + filename)