# GenAI-chatbot-using-LLama

![image](https://github.com/user-attachments/assets/3f877340-a1c8-40a0-a29e-5cfdb8506092)


AI-Powered Real Estate Query Tool

An AI-powered tool that handles real estate queries without any fluff—just straight, reliable results. No more pulling your hair out over generic bot responses. This tool is designed to understand your real estate questions and deliver precise answers in real-time.
Overview

This project leverages cutting-edge AI and machine learning frameworks to deliver accurate, context-aware responses for real estate queries. It integrates multiple state-of-the-art technologies to ensure that every question is answered with precision and speed.
The Setup

    🏠 LLama + GroqAPI
        Purpose: Provides genuine, context-specific answers, moving beyond the generic responses often associated with basic bots.
        Benefit: Understands what you're asking, delivering high-quality, relevant answers.

    🔍 HuggingFace Embeddings
        Purpose: Captures contextual nuances so that responses are tailored to your query.
        Benefit: Ensures that the tool retrieves the most relevant information without irrelevant chatter.

    📜 LangChain + LLama-Index
        Purpose: Processes documents and handles complex queries efficiently.
        Benefit: Seamlessly navigates through large volumes of text, extracting the data you need.

    ⚡ FAISS Vector Database
        Purpose: Enables incredibly fast search and retrieval.
        Benefit: No waiting or lag—quickly finds the information you’re looking for.

    💾 Real Estate Dataset
        Purpose: Provides a robust, domain-specific dataset for real estate queries.
        Benefit: Data is crawled from the web and optimized for real estate insights.

    🚀 Streamlit UI
        Purpose: Offers a clean, user-friendly interface that makes real-time insights accessible.
        Benefit: Intuitive design that requires no advanced technical knowledge—just type your query and get the results.

How It Works

    Query Input:
    The user inputs a real estate-related query via the Streamlit interface.

    Data Processing:
        The query is processed using HuggingFace embeddings to capture the context.
        LangChain and LLama-Index work together to parse and extract relevant information from documents.

    Fast Search:
    FAISS vector database speeds up the retrieval of contextually relevant documents and answers.

    Response Generation:
    LLama integrated with GroqAPI formulates a clear, accurate answer that’s delivered back through the Streamlit UI.

    User Experience:
    The entire process is optimized for speed and clarity—ensuring you get real-time insights without the need for any advanced setup or technical know-how.

Key Takeaways

    Real-World Integration:
    AI integration isn’t as smooth as tutorials often make it seem. Expect challenges—but once the pieces click together, it’s a game changer.

    Efficiency & Precision:
    Combining these tools leads to a highly efficient and accurate real estate query tool that goes far beyond standard bot responses.

    Scalability:
    With fast search capabilities and robust data processing, the system is built to scale and handle complex queries as your needs grow.

Getting Started
Prerequisites

    Python 3.7+
    Required Python packages (listed in requirements.txt)

Installation

    Clone the repository:



Install dependencies:


Run the Streamlit app:

    streamlit run app.py

Contributing

If you have ideas to make this tool even better or want to contribute enhancements, please open an issue or submit a pull request. I'm all ears for collaboration and improvements!
