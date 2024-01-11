import streamlit as st
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
from whoosh import scoring

# Function to create the Whoosh index
def create_search_index():
    schema = Schema(content=TEXT(stored=True))
    index = create_in("index", schema)
    writer = index.writer()

    # Add sample documents to the index
    documents = [
        "Python is a programming language that lets you work quickly and integrate systems more effectively.",
        "Streamlit is a Python library that makes it easy to create web apps for machine learning and data science.",
        "Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python.",
        "Machine learning is a field of artificial intelligence that focuses on the development of algorithms that enable computers to learn from and make predictions or decisions based on data.",
        "Data science is a multidisciplinary field that uses scientific methods, processes, algorithms, and systems to extract insights and knowledge from structured and unstructured data.",
    ]

    for doc in documents:
        writer.add_document(content=doc)

    writer.commit()

# Function to search the index and return the top N results
def search_index(query, top_n=5):
    ix = open_dir("index")
    with ix.searcher(weighting=scoring.BM25F()) as searcher:
        query_parser = QueryParser("content", ix.schema)
        parsed_query = query_parser.parse(query)
        results = searcher.search(parsed_query, limit=top_n)
        return results

# Streamlit app
def main():
    st.title("Search App")

    # Create the index if it doesn't exist
    create_search_index()

    # User input for search query
    search_query = st.text_input("Enter your search query:")

    if search_query:
        # Search the index and get top 5 results
        results = search_index(search_query, top_n=5)

        # Display the results
        st.subheader("Top 5 Most Relevant Cases:")
        for i, result in enumerate(results):
            st.write(f"{i+1}. {result['content']}")

        # Show position of entered entry among top 10 search results
        position_indicator = results.rank(search_query)
        st.subheader(f"Position of entered entry among top 10 search results: {position_indicator}")

if __name__ == "__main__":
    main()
