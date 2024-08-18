from flask import Flask, request, jsonify
from flask_cors import CORS
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
    text = request.args.get('prompt')

    # Check if the 'text' parameter is provided
    if text:
        return jsonify({"message": f"Country: {get_countries(text)}"}), 200
    else:
        return jsonify({"error": "No string provided"}), 400
    
def get_countries(prompt):
    tidb_connection_string = os.environ["TIDB_CONNECTION_STRING"]

    embeddings = OpenAIEmbeddings()

    # Query the Vector Store
    vector_store = TiDBVectorStore.from_existing_vector_table(
        embedding=embeddings,
        connection_string=tidb_connection_string,
        table_name="vectors",
        distance_strategy="cosine",
    )

    # Finds the most similar document to the query
    query = "Find a country with people that speak English and Spanish, with warm weather, with extra hot spicy food, with people that follow Christianity, with a crime index of under 6, with landmarks, with many places for hiking, with broadband download speed of over 50 Mbps, with a tap water index of over 60, with no ongoing conflicts or regional tensions, with political stability and no political tensions, with a government that has a voting system, not in the continents of North America, and specifically not Bangladesh, Libya, Lebanon, Afghanistan, Somalia, Iran, Yemen, Syria, Russia, Myanmar, Venezuela, Iraq, South Sudan, Mali, Central African Republic, Burkina Faso, Haiti, Belarus, North Korea, Ukraine, Sudan, Mexico, Israel, or Palestine State."
    filters = {
        "Crime_Index":{"$lt": 4.5},
        "Download_Speed":{"$gt": 100},
        "Tap_Water_Index":{"$gt": 80},
    }

    docs_with_score = vector_store.similarity_search_with_relevance_scores(query, filter=filters, k=1)
    # docs_with_score = vector_store.similarity_search_with_relevance_scores(query, k=20)
    for doc, score in docs_with_score:
        return doc.page_content