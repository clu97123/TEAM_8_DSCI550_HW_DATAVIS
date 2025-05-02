import os
import json
import re

INPUT_FOLDER = "C:/USC Sem 2/DSCI 550/HW3/imagecat_index"
OUTPUT_FILE = "C:/USC Sem 2/DSCI 550/HW3/bulk_clean.json"

def clean_field_name(name):
    # lowercase, replace spaces and symbols with underscores
    return re.sub(r'[^a-zA-Z0-9_]', '_', name.strip().lower())

all_docs = []

for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".json"):
        with open(os.path.join(INPUT_FOLDER, file), 'r', encoding='utf-8') as f:
            try:
                doc = json.load(f)

                cleaned_doc = {
                    "id": doc.get("id", os.path.basename(file).split('.')[0]),
                    "filename": doc.get("filename", ""),
                    "filepath": doc.get("filepath", ""),
                    "ocr_text": doc.get("ocr_text", "")
                }

                metadata = doc.get("metadata", {})
                for key, value in metadata.items():
                    safe_key = clean_field_name(key)
                    cleaned_doc[safe_key] = value

                all_docs.append(cleaned_doc)

            except Exception as e:
                print(f"Error in {file}: {e}")

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_docs, f, indent=2)
