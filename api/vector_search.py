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
    try:
        prompt = request.args.get('prompt')
        if not prompt:
            raise ValueError("Missing 'prompt' parameter")
        
        crime_index = request.args.get('crime_index', type=float)
        if not crime_index:
            raise ValueError("Missing 'crime_index' parameter")
        
        download_speed = request.args.get('download_speed', type=int)
        if not download_speed:
            raise ValueError("Missing 'download_speed' parameter")
        
        mobile_download_speed = request.args.get('mobile_download_speed', type=int)
        if not mobile_download_speed:
            raise ValueError("Missing 'mobile_download_speed' parameter")
        
        tap_water_index = request.args.get('tap_water_index', type=float)
        if not tap_water_index:
            raise ValueError("Missing 'tap_water_index' parameter")
        
        continent_list = request.args.get('continent_list', type=str)
        if continent_list:
            continent_list = json.loads(continent_list)
        else:  
            raise ValueError("Missing 'continent_list' parameter")
        
        blacklist_countries = request.args.get('blacklist_countries', type=str)
        if blacklist_countries:
            blacklist_countries = json.loads(blacklist_countries)
        else:
            raise ValueError("Missing 'blacklist_countries' parameter")
        
        country = get_countries(prompt, crime_index, download_speed, mobile_download_speed, tap_water_index, continent_list, blacklist_countries)
        return jsonify({"countries": country, "continents_list": continent_list, "blacklist_countries": blacklist_countries}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except json.JSONDecodeError as je:
        return jsonify({"error": "Invalid JSON format", "details": str(je)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500        
    
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