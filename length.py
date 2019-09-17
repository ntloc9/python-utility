import subprocess
import os

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]


for f in os.listdir('/mnt/Code/doc code/reactjs/Part1'):
    print("{} is {} milliseconds long".format(f, getLength(f)))
