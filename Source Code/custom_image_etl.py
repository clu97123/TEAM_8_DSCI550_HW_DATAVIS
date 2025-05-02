import os
import json
import uuid
from tika import parser

# CONFIGURE ME:
INPUT_DIR = r"C:\USC Sem 2\DSCI 550\HW3\images"
OUTPUT_DIR = r"C:\USC Sem 2\DSCI 550\HW3\imagecat_index"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_resource_name(raw_name):
    if raw_name.startswith("b'"):
        return raw_name[2:-1]
    return raw_name

for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(root, file)
            print(f"Processing: {file_path}")

            try:
                parsed = parser.from_file(file_path)

                metadata = parsed.get("metadata", {})
                content = parsed.get("content", "")

                # Generate a unique ID for the image
                image_id = str(uuid.uuid4())

                # Create a Solr-like JSON document
                doc = {
                    "id": image_id,
                    "filename": file,
                    "filepath": file_path,
                    "metadata": metadata,
                    "ocr_text": content.strip() if content else "",
                }

                # Save the JSON
                with open(os.path.join(OUTPUT_DIR, f"{image_id}.json"), "w", encoding='utf-8') as f:
                    json.dump(doc, f, indent=4)

            except Exception as e:
                print(f"Failed to process {file_path}: {e}")
