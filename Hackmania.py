import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample legal knowledge base
knowledge_base = {
    "citizenship": "To apply for citizenship, you need to meet the following requirements: ...",
    "visa": "To apply for a visa, you need to provide the following documents: ...",
    "taxes": "To file your taxes, follow these steps: ...",
    # Add more legal information as needed
}

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

# Function to find the best matching response
def get_response(user_input):
    user_input = preprocess_text(user_input)
    vectorizer = TfidfVectorizer().fit_transform([user_input] + list(knowledge_base.keys()))
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors[0].reshape(1, -1), vectors[1:])
    best_match_index = cosine_sim.argmax()
    return knowledge_base[list(knowledge_base.keys())[best_match_index]]

# Main function to handle user queries
def handle_query(user_query):
    response = get_response(user_query)
    return response

# Example usage
if _name_ == "_main_":
    user_query = "How do I apply for citizenship?"
    response = handle_query(user_query)
    print(response)