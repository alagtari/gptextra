import os

program_path = r'C:\Users\Ala\Desktop\openai'

if os.path.exists(program_path):
    path_dirs = os.environ['PATH'].split(os.pathsep)
    if program_path in path_dirs:
      print(f"{program_path} is in the PATH variable.")
    else:
        print(f"{program_path} is not in the PATH variable.")
        print(f"{program_path} added to the PATH variable.")
else:
    print(f"The program file {program_path} does not exist.")



"""path = os.environ['PATH'].split(os.pathsep)
path.append(program_path)
os.environ['PATH'] =os.pathsep.join(path)
print(os.environ['PATH'].split(os.pathsep))"""

program_path = "C:\Program Files\Tesseract-OCR"
