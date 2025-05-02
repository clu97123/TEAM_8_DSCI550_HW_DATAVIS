==README==
Link to data visualizations website: https://clu97123.github.io/TEAM_8_DSCI550_HW_DATAVIS/


==Division of Work==
Alysa Xu: Task 1, Task 2 (D3 Stacked Bar Chart, Bubble Chart)
Catherine Lu: Task 5 (MEMEX Geoparser)
Justin Huh: Task 1, Task 2 (D3 Calendar Visualization)
Rohan Rane: Task 1, Task 2 (D3 Bar Chart Race, State Chloropleth (Heat Map))
Vishal Menon: Task 4 (Image Space)
Pratham Kambli Task 4 (Image Space)

==List of Libraries==
Below is a list of the following libraries utilized for our project. For each library we went ahead and provided the purpose of the library and why we used it in our project.

=GeoParser==
The GeoParser code includes several shell scripts, a Python notebook, and a CSV file of the haunted places. Docker for Desktop should be installed and opened first. The geoparser-main shell script sets up the MEMEX GeoParser server. The create-core and add-fields shell scripts create a Solr index for the haunted places. The Ingest Data notebook loads a subset of the haunted places data (city, country, location, state, longitude, and latitude) into the Solr index. The Solr index can be added to the MEMEX GeoParser server and create a GeoParser visualization.

jupyterlab: run JupyterLab server to execute Jupyter Notebook
pandas: convert data to DataFrame and manipulate it
pysolr: to create Solr core
requests: necessary to make requests to Solr to ingest data
tqdm: keep track of progress of data ingestion

==D3 Visualizations==
json: to read and write JSON files
IPython.display.HTML: display interactive HTML content in notebooks
matplotlib.pyplot: Creating visualizations (bar charts of monthly/yearly haunted events)

How to Run Visualization Code:

=Calendar=
Open Python notebook titled “DSCI_550_HW3_Task2_Calendar (2).ipynb”
Upload “haunted_places_v2.tsv” file
Run all sections of Python notebook (the first calendar has all data, the second calendar has top 5 years data)

=Bar Chart Race=
Open BAR_CHART_RACE.ipynb
Upload “haunted_places.json” file
Run all sections of the notebook 
Imageio: allows an easy interface to read and write a wide range of image data, including animated images
kaleido: allows you to convert plotly figures to images

=Apparition Count Stacked Bar Chart=
Open “Viz1 - Stacked Bar Chart.ipynb”
Upload “haunted_places.json” file
Run all sections of the notebook 
Open “Visualization 1 - Stacked Bar Chart.tgz” 
Upload the new file and run all the code
Datetime: parse date strings to extract the year for time based analysis
@d3/color-legend: generate SVG legend for color scale in D3
Pprint: print and inspect json file for readability 

=Witness Count Bubble Chart=
Open “Viz3 - Bubble Chart.ipynb”
Upload “haunted_places.json” file
Run all sections of the notebook 
Open “Visualization 3 - Bubble Chart.tgz” 
Upload the new file and run all the code

=Alcohol Abuse Heat Map=
Open “Viz4 - Heat Map.ipynb”
Upload “haunted_places.json” file
Run all sections of the notebook 
Open “Visualization 4 - Heat Map.tgz” 
Upload the new file and run all the code
@d3/color-legend: generate SVG legend for color scale in D3

=Image-Space similar Image generation=
pytorch: A deep learning framework used to load pretrained CNN models like ResNet18 for feature extraction.
torch: The core PyTorch library used to compute image descriptors via neural networks.
smqtk: A toolkit used to generate, store, and compare image descriptors for similarity search.

Install all the requirements
Run the extract_metadata.py on the set of images
Generate Solr-ready metadata using custom_image_et1.py
Launch Solr and post the metadata there
Generate SMQTK image descriptors using generate_descriptors.py
Find similar images using query_faiss.py by editing the query_path
