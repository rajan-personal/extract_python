import os 
from classes import AI, Copy

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = "sample.py"
full_path = dir_path + "/" + file_name

file1 = Copy(full_path)
print(file1.count)
print(file1.read_line(1))