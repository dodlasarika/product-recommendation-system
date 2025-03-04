import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv('products.csv')

# Convert descriptions into numerical vectors
vectorizer = TfidfVectorizer(stop_words='english')
product_vectors = vectorizer.fit_transform(df['Description'])

# Compute similarity between products
similarity_matrix = cosine_similarity(product_vectors)

# Function to recommend products
def recommend_products(product_name):
    if product_name not in df['Product_Name'].values:
        return ["Product not found! Please enter a valid product name."]
    
    # Find the index of the given product
    idx = df[df['Product_Name'] == product_name].index[0]

    # Compute similarity scores for the given product
    similarity_scores = list(enumerate(similarity_matrix[idx]))

    # Sort products based on similarity scores (excluding the first one, which is itself)
    sorted_products = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]  # Getting top 5 similar products

    # Get the recommended product names
    recommendations = [df.iloc[i[0]]['Product_Name'] for i in sorted_products]

    # Debugging: Print similarity scores to check if sorting works correctly
    print(f"\nProduct: {product_name}")
    print("Recommendations:", recommendations)

    return recommendations

# Streamlit UI
st.title("🛒 Product Recommendation System")
st.write("Enter a product name to get recommendations!")

# User input
product_name = st.text_input("Enter a Product Name", "")

if st.button("Get Recommendations"):
    if product_name:
        recommended_products = recommend_products(product_name)
        st.write("### Recommended Products:")
        for prod in recommended_products:
            st.write(f"✅ {prod}")
    else:
        st.write("⚠️ Please enter a product name.")
