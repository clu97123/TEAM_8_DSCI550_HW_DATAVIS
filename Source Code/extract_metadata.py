import os
import pandas as pd
from tika import parser

# Load the TSV file
df = pd.read_csv("output_with_images.tsv", sep="\t")

# Drop rows where image_path is missing
df = df[df['image_path'].notna()]

# Make sure all entries are strings
df['image_path'] = df['image_path'].astype(str)

# Output directory for metadata JSONs
output_dir = "tika_metadata"
os.makedirs(output_dir, exist_ok=True)

for img_path in df['image_path']:
    if not os.path.isfile(img_path):
        print(f"Skipping invalid file path: {img_path}")
        continue
    try:
        parsed = parser.from_file(img_path)
        img_name = os.path.basename(img_path).split('.')[0]
        with open(os.path.join(output_dir, f"{img_name}.json"), 'w', encoding='utf-8') as f:
            f.write(str(parsed))
        print(f"Processed: {img_path}")
    except Exception as e:
        print(f"Failed to parse {img_path}: {e}")

