from wand.image import Image
import os
import subprocess

# TODO: Error handling?
# TODO: Smart resizing

files = [file for file in sorted(os.listdir('.')) if os.path.isfile(file) and file.endswith('.jpg')]

# Protect files that the software guesses are already
# renamed in order to prevent recursive loops.
ignore_resized_name = False

for file in files:
  if not ignore_resized_name and file.endswith("_resized.jpg"):
    print("Skipping {}...".format(file))
    continue

  with Image(filename=file) as img:
    print('Loaded {}'.format(file))
    print(img.width, img.height)
    # TODO: This isn't getting reached?
    if img.width <= 1156 and img.height <= 867:
      continue
    img.resize(1156,867)
    print(img.width, img.height)
    new_filename = file[:-4] + "_resized.jpg"
    img.save(filename=new_filename)

subprocess.run(["img2pdf", "-o", "out.pdf", "*_resized.jpg"])