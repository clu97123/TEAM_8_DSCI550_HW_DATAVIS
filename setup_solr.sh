#!/bin/bash
# setup_solr.sh

# This script sets up Apache Solr using Docker and creates a 'haunted' core.

echo "Starting Solr Docker container..."
docker run -d -p 8983:8983 --name solr solr

# Wait for Solr to start
echo "Waiting for Solr to initialize..."
sleep 10

echo "Creating 'haunted' core..."
docker exec -it solr solr create_core -c haunted

echo "Solr is running on http://localhost:8983"
echo "You can access the core at: http://localhost:8983/solr/#/haunted/query"
