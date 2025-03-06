import os
import pathlib
import shutil
import time



os.mkdir("test_dir")
os.mknod("test.txt")
os.replace("test.txt", "./test_dir/test.txt")
print(f"\rreplace...", end="")
time.sleep(2)
print("\rfile replacing succesful")

print(f"\rremoving...", end="")
time.sleep(2)
shutil.rmtree("test_dir")   #? удаление не пустой директории
print("\rtree removing succesful")

print("-" * 40)

os.mkdir("Test_dir")
print(f"\rmaking node...", end="")
time.sleep(2)
os.mknod("./Test_dir/Test_file.txt")
print("\rnode making succesfull")
print(f"\rremoving...", end="")
time.sleep(2)
shutil.rmtree("Test_dir")   #? удаление не пустой директории
print("\rtree removing succesful")
