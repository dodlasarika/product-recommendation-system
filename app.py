import streamlit as st
import pandas as pd
import difflib  # For better product name matching
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the cleaned dataset
df = pd.read_csv('cleaned_amazon_products.csv')

# Convert 'rating' to numeric (since it was stored as a string)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Fill any remaining NaN values with the mean rating
df['rating'].fillna(df['rating'].mean(), inplace=True)

# Convert descriptions into numerical vectors
vectorizer = TfidfVectorizer(stop_words='english')
product_vectors = vectorizer.fit_transform(df['about_product'])

# Compute similarity between products
similarity_matrix = cosine_similarity(product_vectors)

# Function to recommend products
def recommend_products(product_name):
    # Use fuzzy matching to find the closest product name
    possible_matches = difflib.get_close_matches(product_name, df['product_name'], n=1, cutoff=0.4)

    if not possible_matches:
        return ["Product not found! Please enter a valid product name."]

    product_name = possible_matches[0]  # Take the best match
    
    # Find the index and category of the matched product
    idx = df[df['product_name'] == product_name].index[0]
    product_category = df.iloc[idx]['category']

    st.write(f"🔍 Searching recommendations for: {product_name} (Category: {product_category})")

    # Filter products from the same category
    category_filtered_df = df[df['category'] == product_category].reset_index(drop=True)

    # Compute similarity only within this filtered category
    vectorizer = TfidfVectorizer(stop_words='english')
    product_vectors = vectorizer.fit_transform(category_filtered_df['about_product'])
    similarity_matrix_filtered = cosine_similarity(product_vectors)

    # Find the new index of the given product inside the filtered dataframe
    new_idx = category_filtered_df[category_filtered_df['product_name'] == product_name].index[0]

    # Compute similarity scores
    similarity_scores = list(enumerate(similarity_matrix_filtered[new_idx]))

    # Sort products based on similarity scores and rating
    sorted_products = sorted(
        similarity_scores, 
        key=lambda x: (x[1], category_filtered_df.iloc[x[0]]['rating']), 
        reverse=True
    )[1:4]  # Top 3 recommendations

    # Get recommended product names and remove duplicates
    recommendations = []
    seen = set()
    for i in sorted_products:
        product = category_filtered_df.iloc[i[0]]['product_name']
        if product not in seen:
            recommendations.append(product)
            seen.add(product)

    return recommendations

# Streamlit UI
st.title("🛒 Amazon Product Recommendation System")
st.write("Enter a product name to get recommendations!")

# User input
product_name = st.text_input("Enter a Product Name", "")

if st.button("Get Recommendations"):
    if product_name:
        with st.spinner("Generating recommendations..."):
            recommended_products = recommend_products(product_name)
            st.write("### Recommended Products:")
            for prod in recommended_products:
                st.write(f"✅ {prod}")
    else:
        st.write("⚠️ Please enter a product name.")



