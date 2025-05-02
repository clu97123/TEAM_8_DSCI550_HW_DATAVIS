import os
import glob
import numpy as np
from smqtk_descriptors.impls.descriptor_generator.torchvision_model import TorchvisionImageDescriptorGenerator
from PIL import Image

# CONFIG
IMG_FOLDER = "images"
DESCRIPTOR_FOLDER = "descriptors"
os.makedirs(DESCRIPTOR_FOLDER, exist_ok=True)

# Init model
generator = TorchvisionImageDescriptorGenerator('resnet18', device='cpu')

# Get all image paths
image_paths = glob.glob(os.path.join(IMG_FOLDER, "*.*"))

for img_path in image_paths:
    try:
        img = Image.open(img_path).convert("RGB")
        descriptor = generator.generate_arrays(img)[0]

        uid = os.path.splitext(os.path.basename(img_path))[0]
        out_path = os.path.join(DESCRIPTOR_FOLDER, f"{uid}.npy")

        np.save(out_path, descriptor)
        print(f"✅ Descriptor saved for {uid}")

    except Exception as e:
        print(f"❌ Failed to process {img_path}: {e}")
