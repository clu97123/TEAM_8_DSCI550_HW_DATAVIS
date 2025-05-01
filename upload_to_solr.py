import requests
import json

def safe_float(val):
    try:
        return float(val)
    except:
        return None

# Load JSON data
with open("/Users/Vishal/Downloads/HauntedData/haunted_places.json") as f:
    data = json.load(f)

# Clean problematic fields
for record in data:
    record["moon_phase"] = safe_float(record.get("moon_phase"))
    record["moon_diameter"] = safe_float(record.get("moon_diameter"))
    record["moon_distance"] = safe_float(record.get("moon_distance"))
    record["Alcohol deaths per capita"] = safe_float(record.get("Alcohol deaths per capita"))
    record["Annual deaths attributable to excessive alcohol use"] = safe_float(record.get("Annual deaths attributable to excessive alcohol use"))
    record["Population"] = safe_float(record.get("Population"))
    record["Housing Units"] = safe_float(record.get("Housing Units"))
    record["Median Age"] = safe_float(record.get("Median Age"))

url = "http://localhost:8983/solr/haunted/update?commit=true"
headers = {"Content-Type": "application/json"}

# Upload in batches
for i in range(0, len(data), 100):
    batch = data[i:i+100]
    response = requests.post(url, headers=headers, data=json.dumps(batch))
    print(f"Batch {i//100 + 1}: {response.status_code}, {response.text}")
