Blog to Podcast Agent
Convert blog articles into spoken podcast episodes using OpenAI, ElevenLabs, and Firecrawl.

Overview
This Streamlit app allows users to enter the URL of a blog post and automatically converts the content into a podcast-style audio file. It uses:

OpenAI for language processing and summarization.

ElevenLabs for realistic text-to-speech synthesis.

Firecrawl for web scraping and article extraction.

Features
User-friendly web interface built with Streamlit.

Accepts blog URLs and converts them to podcasts.

Realistic voice synthesis using ElevenLabs.

Secure entry of API keys.

Automatically saves audio output locally.

Requirements
Python 3.7 or higher

API keys for:

OpenAI

ElevenLabs

Firecrawl

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/blog-to-podcast-agent.git
cd blog-to-podcast-agent
(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run the Streamlit application:

bash
Copy
Edit
streamlit run "blog_to_podcast_agent day 1.py"
Enter your API keys in the sidebar input fields.

Paste the blog URL into the input field.

Click the "Generate Podcast" button to start the process.

The app will generate and download the audio file.

Project Structure
css
Copy
Edit
blog-to-podcast-agent/
├── blog_to_podcast_agent day 1.py
├── README.md
└── requirements.txt
API Key Management
Do not hardcode your API keys into the script. Use the secure input fields provided by the Streamlit interface.
