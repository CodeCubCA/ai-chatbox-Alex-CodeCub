import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Study Buddy AI Assistant v2.0",
    page_icon="📚",
    layout="wide"
)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    """Initialize Groq API client"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ **GROQ_API_KEY is missing!**")
        st.info("""
        **For Streamlit Cloud:**
        1. Go to your app settings
        2. Click on "Secrets" in the left sidebar
        3. Add your Groq API key:
        ```
        GROQ_API_KEY = "your_groq_api_key_here"
        ```
        4. Click "Save"

        **For local development:**
        1. Copy `.env.example` to `.env`
        2. Add your Groq API key to the `.env` file

        Get your free API key at: https://console.groq.com/keys
        """)
        st.stop()
    return Groq(api_key=api_key)

client = init_groq_client()

# AI Personality Settings
PERSONALITIES = {
    "Friendly": {
        "name": "Friendly 😊",
        "icon": "😊",
        "description": "Warm and friendly, chat like friends",
        "system_prompt": """You are a warm and friendly Study Buddy AI assistant. Your characteristics:
- Communicate with a warm, encouraging tone like a good friend
- Use positive and supportive language frequently
- Show understanding and support for learning difficulties
- Explain complex concepts in simple, easy-to-understand ways
- Use emojis appropriately to make conversations more engaging
- Care about the user's learning progress and feelings"""
    },
    "Professional": {
        "name": "Professional 🎓",
        "icon": "🎓",
        "description": "Rigorous and professional, give accurate advice",
        "system_prompt": """You are a professional and rigorous Study Buddy AI assistant. Your characteristics:
- Use professional, accurate terminology and expressions
- Provide structured, well-organized answers
- Focus on details and accuracy
- Give systematic learning suggestions and methods
- Reference reliable learning theories and methods
- Maintain an objective and professional attitude"""
    },
    "Humorous": {
        "name": "Humorous 😄",
        "icon": "😄",
        "description": "Relaxed and humorous, interesting chat",
        "system_prompt": """You are a relaxed and humorous Study Buddy AI assistant. Your characteristics:
- Communicate with a light and lively tone
- Add appropriate humor and interesting analogies
- Explain boring knowledge in fun ways
- Use emojis and witty remarks frequently
- Make the learning process fun and engaging
- But maintain accuracy on key knowledge points"""
    }
}

# Sidebar Settings
with st.sidebar:
    st.title("📚 Study Buddy Settings")

    # Welcome message
    st.markdown("""
    ### 👋 Welcome to Study Buddy!

    I'm your AI learning assistant, here to help you with:
    - 📖 Answering study questions
    - 💡 Explaining complex concepts
    - ✍️ Tutoring homework and essays
    - 🎯 Creating study plans
    - 📝 Summarizing and reviewing topics
    - 🧠 Providing learning method suggestions

    Choose your preferred AI personality and start your learning journey!
    """)

    st.divider()

    # AI Personality Selection
    st.subheader("🎭 Select AI Personality")

    personality_choice = st.radio(
        "Choose your preferred communication style:",
        options=list(PERSONALITIES.keys()),
        format_func=lambda x: f"{PERSONALITIES[x]['icon']} {PERSONALITIES[x]['name']}",
        help="Different personalities will affect AI's response style"
    )

    # Display current personality description
    st.info(f"**{PERSONALITIES[personality_choice]['description']}**")

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # Footer info
    st.markdown("---")
    st.caption("💻 Powered by Groq API")
    st.caption("🤖 Model: llama-3.3-70b-versatile")

# Main Title
st.title("📚 Study Buddy AI Assistant v2.0")
st.markdown(f"**Current Personality:** {PERSONALITIES[personality_choice]['icon']} {PERSONALITIES[personality_choice]['name']}")
st.divider()

# Version info (helps trigger redeployment)
# v2.0.0

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("💬 Ask your study question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Build message history with system prompt
        messages_for_api = [
            {"role": "system", "content": PERSONALITIES[personality_choice]["system_prompt"]}
        ]
        messages_for_api.extend(st.session_state.messages)

        try:
            # Call Groq API (streaming)
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages_for_api,
                temperature=0.7,
                max_tokens=2048,
                stream=True
            )

            # Stream response
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")
            full_response = "Sorry, I encountered an issue. Please try again later."
            message_placeholder.markdown(full_response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
