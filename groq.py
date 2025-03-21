import streamlit as st
from llama_index.core import VectorStoreIndex
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    ServiceContext,
    load_index_from_storage
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.groq import Groq


GROQ_API_KEY = "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"

pdf_files = ["C:\\Users\\Nirbhay Singh\\OneDrive\\Desktop\\LlamaProject\\sector.pdf"]


# Function to load documents and create the index
def create_index():
    reader = SimpleDirectoryReader(input_files=pdf_files)
    documents = reader.load_data()
    
    text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=200)
    nodes = text_splitter.get_nodes_from_documents(documents, show_progress=True)

    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    llm = Groq(model="llama-3.3-70b-specdec", api_key=GROQ_API_KEY)

    service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)

    vector_index = VectorStoreIndex.from_documents(documents, show_progress=True, service_context=service_context, node_parser=nodes)
    vector_index.storage_context.persist(persist_dir="./storage_mini")

    storage_context = StorageContext.from_defaults(persist_dir="./storage_mini")
    index = load_index_from_storage(storage_context, service_context=service_context)
    
    return index

# Initialize Streamlit UI components
st.set_page_config(page_title="Real Estate Chatbot", page_icon="🏠", layout="wide")

# Title and Description
st.title("🏠 Delhi-NCR Real Estate  Chatbot")
st.markdown(
    """
    Welcome to Delhi - NCR !  

    I am your Broker for all the properties in this area
    Ask any question related to the real estate market in Delhi - NCR, and get instant answers without any commision.
    """
)

# Sidebar for additional information
with st.sidebar:
    st.header("About the Chatbot")
    st.write(
        """
        This chatbot is developed by Nirbhay
        It's the modern broker for all the properties in Delhi- NCR
        
        Soon will be avalaible for Cities like Lucknow , Mumbai and other cities.
        """
    )
    st.markdown("---")
    st.info("Tip: Only ask Questions related to Delhi-NCR area for now")

# Input field for the query
st.markdown("### Ask your question below:")
query = st.text_input("Type your query:", placeholder="e.g., What are the current property prices in Gurugram?")

# Display response or errors
if query:
    with st.spinner("Processing your query..."):
        try:
            # Create the index if it doesn't exist
            index = create_index()
            query_engine = index.as_query_engine(service_context=index.service_context)
            
            # Get response from the query engine
            resp = query_engine.query(query)
            
            # Display the response
            st.success("Let me know if you need help about more property related questions:")
            st.write(resp.response)
        
        except Exception as e:
            st.error("Oops! Something went wrong.")
            st.write("Error details:", str(e))