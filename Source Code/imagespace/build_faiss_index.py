import os
import faiss
import numpy as np
import pickle

DESCRIPTOR_FOLDER = "descriptors"
INDEX_FILE = "faiss.index"
UID_MAP_FILE = "uid_to_img.pkl"

# 1. Load all descriptor .npy files
descriptor_paths = sorted([
    os.path.join(DESCRIPTOR_FOLDER, f)
    for f in os.listdir(DESCRIPTOR_FOLDER)
    if f.endswith(".npy")
])

descriptors = []
uid_to_img = []

for path in descriptor_paths:
    vec = np.load(path).astype("float32")
    descriptors.append(vec)
    uid = os.path.splitext(os.path.basename(path))[0]
    uid_to_img.append(uid)

descriptors = np.stack(descriptors)

# 2. Build FAISS index
index = faiss.IndexFlatL2(descriptors.shape[1])  # L2 similarity
index.add(descriptors)

# 3. Save index and UID mapping
faiss.write_index(index, INDEX_FILE)
with open(UID_MAP_FILE, "wb") as f:
    pickle.dump(uid_to_img, f)

print(f"✅ FAISS index built with {len(descriptors)} vectors.")
