import shutil
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

source_path = arg1
target_path = arg2

shutil.copytree(source_path,target_path)

