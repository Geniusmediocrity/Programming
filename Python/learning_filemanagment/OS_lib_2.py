import os
import pathlib
import shutil
import time



os.mkdir("test_dir")
os.mknod("test.txt")
time.sleep(1)
os.replace("test.txt", "./test_dir/test.txt")
print("file removing succesful")
shutil.rmtree("test_dir")


os.mkdir("Test_dir")
os.chdir("./Test_dir")
os.mknod("Test_file.txt")
os.chdir("..")
time.sleep(2)
shutil.rmtree("Test_dir")   #? удаление не пустой директории

