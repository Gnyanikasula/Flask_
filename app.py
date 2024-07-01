
from flask import Flask, request, jsonify
import pickle
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

app = Flask(__name__)

# Initialize the embedding model
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the FAISS index and descriptions
vector_store = FAISS.load_local('faiss_index', embeddings=model, allow_dangerous_deserialization=True)
with open('descriptions.pkl', 'rb') as f:
    descriptions = pickle.load(f)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query')
    
    # Generate embedding for the user query
    user_embedding = model.embed_documents([user_query])
    
    # Search the FAISS index
    results = vector_store.similarity_search(user_query, k=1)  # Retrieve top 1 result
    retrieved_descriptions = [result.page_content for result in results]
    
    return jsonify({"results": retrieved_descriptions})

if __name__ == '__main__':
    app.run(debug=False, port=5000)

