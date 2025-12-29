import streamlit as st
import ollama

def main():
    st.set_page_config(page_title="Local AI Content Generator", page_icon="📝", layout="wide")

    st.title("📝 Local AI Content Generator")
    st.markdown("Generate text content locally using **Ollama** LLMs. No internet or API keys required.")

   
    with st.sidebar:
        st.header("Configuration")
        
        if st.button("🔄 Refresh Models"):
            st.rerun()

        
        try:
            models_info = ollama.list()
            
           
            if hasattr(models_info, 'models'):
                data = models_info.models
            else:
                data = models_info.get('models', [])

            model_options = []
            for m in data:
                
                if isinstance(m, dict):
                    name = m.get('name') or m.get('model')
                else:
                    name = getattr(m, 'name', getattr(m, 'model', None))
                if name:
                    model_options.append(name)

            if not model_options:
                model_options = ["llama3.2", "mistral", "llama3", "gemma:2b"]
        except Exception as e:
           
            model_options = ["llama3.2", "mistral", "llama3", "gemma:2b"]
            st.error(f"⚠️ **Ollama is not running.**\n\nError details: {e}\n\n1. Check if the black 'Ollama Server' window is open.\n2. Click **'🔄 Refresh Models'** above.")

        selected_model = st.selectbox("Select Model", model_options)

   
        content_type = st.selectbox(
            "Content Type",
            ["Blog Post", "LinkedIn Post", "Twitter Thread", "Email Newsletter", "Product Description", "Essay"]
        )

      
        tone = st.selectbox(
            "Tone",
            ["Professional", "Casual", "Humorous", "Enthusiastic", "Academic", "Persuasive"]
        )

  
    topic = st.text_area("Topic / Description", placeholder="e.g., The benefits of adopting local AI for privacy...", height=150)

    if st.button("Generate Content", type="primary"):
        if not topic.strip():
            st.error("Please enter a topic to proceed.")
            return

        prompt = f"Write a {tone.lower()} {content_type} about the following topic:\n\n{topic}\n\nEnsure the output is formatted in Markdown."

        with st.spinner(f"Generating content with {selected_model}..."):
            try:
                response = ollama.chat(model=selected_model, messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ])
                
                content = response['message']['content']
                
                st.subheader("Generated Result")
                st.markdown(content)
                
            except Exception as e:
                st.error(f"Error connecting to Ollama: {str(e)}")
                st.info("Troubleshooting: Ensure Ollama is installed and running (`ollama serve`).")

if __name__ == "__main__":
    main()