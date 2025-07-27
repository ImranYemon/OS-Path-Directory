
import os
file_path = os.path.abspath(__file__)
print("Full path of this script:", file_path)

directory = os.path.dirname(file_path)
print("Directory of this script:", directory)