from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import TiDBVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/vector_search', methods=['GET'])
def vector_search():
    # Get the 'text' parameter from the request
    prompt = request.args.get('prompt')
    crime_index = request.args.get('crime_index', type=float)
    download_speed = request.args.get('download_speed', type=float)
    mobile_download_speed = request.args('mobile_download_speed', type=float)
    tap_water_index = request.args.get('tap_water_index', type=float)
    continent_list = json.loads(request.args.get('continent_list', type=str))
    blacklist_countries = json.loads(request.args.get('blacklist_countries', type=str))

    # Check if the 'text' parameter is provided
    if prompt is not None and crime_index is not None and download_speed and mobile_download_speed is not None is not None and tap_water_index is not None and continent_list is not None and blacklist_countries is not None:
        country = get_countries(prompt, crime_index, download_speed, mobile_download_speed, tap_water_index, continent_list, blacklist_countries)
        return jsonify({"countries": country, "continents_list": continent_list, "blacklist_countries": blacklist_countries}), 200
    else:
        return jsonify({"error": "No string provided", "countries": country, "continents_list": continent_list, "blacklist_countries": blacklist_countries}), 400
    
def get_countries(prompt, crime_index, download_speed, mobile_download_speed, tap_water_index, continent_list, blacklist_countries):
    tidb_connection_string = os.environ["TIDB_CONNECTION_STRING"]

    embeddings = OpenAIEmbeddings()

    # Query the Vector Store
    vector_store = TiDBVectorStore.from_existing_vector_table(
        embedding=embeddings,
        connection_string=tidb_connection_string,
        table_name="vectors",
        distance_strategy="cosine",
    )
    
    # Applies the filters to the query
    filters = {
        "Crime_Index": {"$lt": crime_index},
        "Download_Speed": {"$gt": download_speed},
        "Mobile_Download_Speed": {"$gt": mobile_download_speed},
        "Tap_Water_Index": {"$gt": tap_water_index},
        "Continent": {"$nin": continent_list},
        "Country": {"$nin": blacklist_countries}
    }

    docs_with_score = vector_store.similarity_search_with_relevance_scores(prompt, filter=filters, k=10)
    # docs_with_score = vector_store.similarity_search_with_relevance_scores(query, k=20)
    countries = []
    for doc, score in docs_with_score:
        # return doc.page_content
        countries.append(doc.metadata['Country'])
    
    return countries