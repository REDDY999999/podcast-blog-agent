import streamlit as st
from firecrawl import FireCrawl
import openai
from elevenlabs import set_api_key, generate, save
import os

# App title
st.title("Blog to Podcast Agent")

# Sidebar: API keys
st.sidebar.header("API Key Configuration")
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
elevenlabs_key = st.sidebar.text_input("ElevenLabs API Key", type="password")
firecrawl_key = st.sidebar.text_input("Firecrawl API Key", type="password")

# Initialize clients if keys provided
if openai_key:
    openai.api_key = openai_key
if elevenlabs_key:
    set_api_key(elevenlabs_key)

# Input: blog URL
url = st.text_input("Enter Blog URL:")

# Voice selection
available_voices = ["Rachel", "Domi", "Bella"]  # update with your ElevenLabs voices
voice = st.selectbox("Select Voice:", available_voices)

# Generate button
if st.button("Generate Podcast"):
    if not (openai_key and elevenlabs_key and firecrawl_key):
        st.error("Please provide all API keys in the sidebar.")
    elif not url:
        st.error("Please enter a valid blog URL.")
    else:
        with st.spinner("Fetching and processing blog content..."):
            try:
                # Extract article text
                crawler = FireCrawl(api_key=firecrawl_key)
                article = crawler.extract(url)
                text = article.get('text', '')
                if not text:
                    st.error("Failed to extract article text. Please check the URL.")
                    st.stop()

                # Summarize or refine with OpenAI
                prompt = (
                    f"You are a helpful assistant that transforms blog posts into conversational podcast scripts. "
                    f"Rewrite the following text as a spoken podcast script, making it engaging and succinct:\n\n{text}"
                )
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=1500
                )
                script = response.choices[0].message.content

                # Generate audio with ElevenLabs
                st.info("Synthesizing voice...")
                audio_bytes = generate(text=script, voice=voice)

                # Save locally
                output_dir = "podcasts"
                os.makedirs(output_dir, exist_ok=True)
                filename = os.path.join(output_dir, f"podcast_{int(st.time())}.mp3")
                save(audio_bytes, filename)

                # Playback and download
                st.success("Podcast generated successfully!")
                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(f"[Download the podcast file]({filename})")

            except Exception as e:
                st.error(f"An error occurred: {e}")
