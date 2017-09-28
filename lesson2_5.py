import os
import subprocess
import shutil

def prepare_dir(path="Result"):
    if not os.path.exists(path):
        os.mkdir(path)

def get_images(path="Source"):
    result = []
    for f in os.listdir(path):
        if os.path.splitext(f)[1] == ".jpg":
            result.append(f)  
    return result

def convert_image(source, target, width=200):
    print("converting: %s %s"%(source, target))
    shutil.copy(source, target)
    subprocess.run(["sips", "--resampleWidth", str(width), target])

def convert_images(images, source_dir="Source", target_dir="Result"):
    for f in images:
        convert_image(os.path.join(source_dir, f), os.path.join(target_dir, f))

if __name__ == "__main__":
    prepare_dir()
    convert_images(get_images())
    