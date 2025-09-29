import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from services.context_service import set_context, get_context

# Load a pre-trained model. This will be downloaded on first run.
# 'all-MiniLM-L6-v2' is a great, lightweight model.
model = SentenceTransformer('all-MiniLM-L6-v2')

try:
    faq_data = pd.read_csv('data/faq_data.csv', encoding='latin1')
    # Pre-calculate embeddings for all questions in your CSV
    question_embeddings = model.encode(faq_data['question'].tolist())
except FileNotFoundError:
    faq_data = pd.DataFrame(columns=['question', 'answer'])
    question_embeddings = np.array([])
    print("WARNING: data/faq_data.csv not found.")

def get_answer(query, chat_id):
    # Try searching with context if available
    last_topic = get_context(chat_id)
    search_query = query
    if last_topic:
        # If the query is short 
        if len(query.split()) < 4:
            search_query = last_topic + " " + query
            print(f"Using context for search: '{search_query}'")

    # Encode the user's query into an embedding
    query_embedding = model.encode([query])

    # Calculate cosine similarity between user query and all FAQ questions
    similarities = cosine_similarity(query_embedding, question_embeddings)

    # Find the index of the most similar question
    most_similar_index = np.argmax(similarities)

    # Define a similarity threshold
    confidence_threshold = 0.6 # You can tune this value

    if similarities[0][most_similar_index] > confidence_threshold:
        answer = faq_data.iloc[most_similar_index]['answer']
        topic = faq_data.iloc[most_similar_index]['topic']
        
        # Save the topic of this successful answer as the new context
        set_context(chat_id, topic)
        return answer
    else:
        # if the search with context fails, then try without context
        if last_topic and search_query != query:
            query_embedding = model.encode([query])
            similarities = cosine_similarity(query_embedding, question_embeddings)
            most_similar_index = np.argmax(similarities)
            if similarities[0][most_similar_index] > confidence_threshold:
                answer = faq_data.iloc[most_similar_index]['answer']
                topic = faq_data.iloc[most_similar_index]['topic']
                set_context(chat_id, topic)
                return answer
        # if all searches fails
        return "Sorry, I don't have an answer for that. For more information, please contact the college administration."    
