# TEAM_8_DSCI550_HW_DATAVIS
\==README==

Link to data visualizations website: [https://clu97123.github.io/TEAM\_8\_DSCI550\_HW\_DATAVIS/](https://clu97123.github.io/TEAM_8_DSCI550_HW_DATAVIS/)

\==Division of Work==

Alysa Xu: Task 1, Task 2 (D3 Stacked Bar Chart, Bubble Chart)

Catherine Lu: Task 5 (MEMEX Geoparser)

Justin Huh: Task 1, Task 2 (D3 Calendar Visualization)

Rohan Rane: Task 1, Task 2 (D3 Bar Chart Race, State Chloropleth (Heat Map))

Vishal Menon: Task 3 (Solr Data Ingestion), Task 4 (Image Space)

Pratham Kambli Task 4 (Image Space)

\==List of Libraries==

Below is a list of the following libraries utilized for our project. For each library we went ahead and provided the purpose of the library and why we used it in our project.

\=GeoParser==

The GeoParser code includes several shell scripts, a Python notebook, and a CSV file of the haunted places. Docker for Desktop should be installed and opened first. The geoparser-main shell script sets up the MEMEX GeoParser server. The create-core and add-fields shell scripts create a Solr index for the haunted places. The Ingest Data notebook loads a subset of the haunted places data (city, country, location, state, longitude, and latitude) into the Solr index. The Solr index can be added to the MEMEX GeoParser server and create a GeoParser visualization.

jupyterlab: run JupyterLab server to execute Jupyter Notebook

pandas: convert data to DataFrame and manipulate it

pysolr: to create Solr core

requests: necessary to make requests to Solr to ingest data

tqdm: keep track of progress of data ingestion

\==D3 Visualizations==

json: to read and write JSON files

IPython.display.HTML: display interactive HTML content in notebooks

matplotlib.pyplot: Creating visualizations (bar charts of monthly/yearly haunted events)

**How to Run Visualization Code:**

\=Calendar=

1.  Open Python notebook titled “DSCI\_550\_HW3\_Task2\_Calendar (2).ipynb”
    
2.  Upload “haunted\_places\_v2.tsv” file
    
3.  Run all sections of Python notebook (the first calendar has all data, the second calendar has top 5 years data)
    

\=Bar Chart Race=

1.  Open BAR\_CHART\_RACE.ipynb
    
2.  Upload “haunted\_places.json” file
    
3.  Run all sections of the notebook 
    

Imageio: allows an easy interface to read and write a wide range of image data, including animated images

kaleido: allows you to convert plotly figures to images

\=Apparition Count Stacked Bar Chart=

1.  Open “Viz1 - Stacked Bar Chart.ipynb”
    
2.  Upload “haunted\_places.json” file
    
3.  Run all sections of the notebook 
    
4.  Open “Visualization 1 - Stacked Bar Chart.tgz” 
    
5.  Upload the new file and run all the code
    

Datetime: parse date strings to extract the year for time based analysis

@d3/color-legend: generate SVG legend for color scale in D3

Pprint: print and inspect json file for readability 

\=Witness Count Bubble Chart=

1.  Open “Viz3 - Bubble Chart.ipynb”
    
2.  Upload “haunted\_places.json” file
    
3.  Run all sections of the notebook 
    
4.  Open “Visualization 3 - Bubble Chart.tgz” 
    
5.  Upload the new file and run all the code
    

\=Alcohol Abuse Heat Map=

1.  Open “Viz4 - Heat Map.ipynb”
    
2.  Upload “haunted\_places.json” file
    
3.  Run all sections of the notebook 
    
4.  Open “Visualization 4 - Heat Map.tgz” 
    
5.  Upload the new file and run all the code
    

@d3/color-legend: generate SVG legend for color scale in D3

\=Image-Space similar Image generation=

pytorch: A deep learning framework used to load pretrained CNN models like ResNet18 for feature extraction.

torch: The core PyTorch library used to compute image descriptors via neural networks.

smqtk: A toolkit used to generate, store, and compare image descriptors for similarity search.

1.  Install all the requirements
    
2.  Run the extract\_metadata.py on the set of images
    
3.  Generate Solr-ready metadata using custom\_image\_et1.py
    
4.  Launch Solr and post the metadata there
    
5.  Generate SMQTK image descriptors using generate\_descriptors.py
    
6.  Find similar images using query\_faiss.py by editing the query\_path
