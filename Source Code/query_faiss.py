import faiss
import numpy as np
import pickle
from PIL import Image
from smqtk_descriptors.impls.descriptor_generator.torchvision_model import TorchvisionImageDescriptorGenerator
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Load FAISS index and UID map
index = faiss.read_index("faiss.index")
with open("uid_to_img.pkl", "rb") as f:
    uid_to_img = pickle.load(f)

# Load your descriptor generator
generator = TorchvisionImageDescriptorGenerator('resnet18', device='cpu')

# Query image (change to any image path)
query_path = "images/woodland_park_colorado_10991.png"
query_img = Image.open(query_path).convert("RGB")

# Get descriptor for query image
query_vector = generator.generate_arrays(query_img)[0].astype("float32").reshape(1, -1)

# Perform FAISS search
k = 5  # Top 5 results
D, I = index.search(query_vector, k)

# Show results
print(f"\n🔎 Top {k} similar images to {query_path}:\n")
for rank, idx in enumerate(I[0]):
    uid = uid_to_img[idx]
    print(f"{rank+1}. {uid} (distance={D[0][rank]:.4f})")
