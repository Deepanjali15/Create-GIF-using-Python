import imageio.v3 as iio
from PIL import Image
import numpy as np
import os
import glob

# Automatically get all images in the "images" folder
image_folder = "images"
filenames = sorted(glob.glob(os.path.join(image_folder, "*.jpg")) +
                   glob.glob(os.path.join(image_folder, "*.jpeg")) +
                   glob.glob(os.path.join(image_folder, "*.png")))



images = []
target_size = (500, 500)  # Resize all images to this size (width, height)

for filename in filenames:
    if not os.path.exists(filename):
        print(f"⚠️ Skipping {filename}: File not found")
        continue

    img = Image.open(filename)
    img = img.resize(target_size)
    img = np.array(img)

    # Ensure consistent color channels (convert grayscale to RGB)
    if img.ndim == 2:
        img = np.stack([img] * 3, axis=-1)

    images.append(img)

# Save as GIF
if images:
    output_name = "team.gif"
    iio.imwrite(output_name, images, duration=200, loop=0)
    print(f"✅ GIF created successfully: {output_name}")
else:
    print("❌ No images were processed.")