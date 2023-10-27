import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="I Am Jason Lowborn", page_icon=":computer:", layout="wide")

# --- FUNCTIONS ---
def load_lottie(url):
    """Load lottie animation from external URL."""
    response = requests.get(url)
    if response.status_code != 200:
        return
    return response.json()

def load_style(file):
    """Load local CSS file."""
    with open(file) as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def load_view(file):
    with open(file) as file:
        st.markdown(file.read(), unsafe_allow_html=True)

load_style("style/style.css")

# --- ASSETS ---
lottie_hacker = load_lottie("https://lottie.host/85e367a8-3cf3-401a-b6bb-27db210d1999/wfYF9BplRP.json")
img_kayn = Image.open("images/kayn.png")
img_dice = Image.open("images/dice.png")
img_github = Image.open("images/github.png")
img_dome = Image.open("images/high_dome.png")

# --- CHART ITEMS ---
hard_skills = {
    'Forensics': 8,
    'Red Teaming': 7,
    'Web Hacking': 8,
    'Threat Intelligence': 6,
    'Programming':  9,
    'Reverse Engineering': 5,
}
soft_skills = { 
    'Communication': 8,
    'Commitment': 9,
    'Cooperation': 8,
    'Presentation': 7,
    'Empathy':  8,
    'Critical Thinking': 10
}

# --- HEADER ---
with st.container():
    st.subheader("Hello, I am Jason Lowborn :wave:")
    st.title("Ethical hacker, freetime developer and gamer.")
    st.write("Passionate cybersecurity enthusiast dedicated to enhancing red teaming expertise.")
    st.write("[LinkedIn](https://www.linkedin.com/in/carlosjesus46/)")

# --- ABOUT ME ---
with st.container():
    st.write("#")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("#####")
        st.write(
            """
            My name is Carlos Jesus, but I go by the alias Jason Lowborn. Inspired by movies and games, I've been studying to become a hacker since I was 14. Since my graduation, I've developed a passion for forensics, offensive security, web hacking, threat intelligence, and programming. However, my primary focus is on becoming a professional red teamer. For this reason, I'm currently studying phishing techniques, social engineering tactics, and Active Directory hacking. I'm always eager to learn more and improve.
            """
        )
        st.markdown(
            """
            > *"The world is full of fascinating problems waiting to be solved."*
            >
            > &mdash; Eric Raymond, *The New Hacker Dictionary*
            """
        )
    with right_column:
        st_lottie(lottie_hacker, height=350, key="hacking")

# --- SKILL SET ---
with st.container():
    st.header("Skill Set")
    st.write("######")
    col1, col2, col3, col4 = st.columns((1,2,1,2), gap="large")

    for skill, level in hard_skills.items():
        with col1:
            st.write(skill)
        with col2:
            st.progress(level / 10)

    for skill, level in soft_skills.items():
        with col3:
            st.write(skill)
        with col4:
            st.progress(level / 10)

# --- PROJECTS ---
with st.container():    # MISP Report Integrator
    st.write("#")
    st.header("Personal Projects")
    st.write("#####")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_dome)
    with text_column:
        st.subheader("MISP Report Integrator")
        st.write(
            """
            As proposed by my instructors during my Cybersecurity Bachelor's program, this tool is designed to collect Indicators of Compromise (IOCs) and generate a report that will subsequently be integrated into the MISP platform, necessitating the use of the MISP API. For a clear understanding and efficient code development, Python was chosen as the programming language. This project was awarded the first place prize, which is the equivalent of R$5000,00.
            """
        )
        st.write("[Github Repository](https://github.com/Alta-Cupula/MISP-Report-Integrator)")

with st.container():    # Kayn EML Parser
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_kayn)
    with text_column:
        st.subheader("Kayn EML Parser")
        st.write(
            """
            Inspired by the original bash script, Kayn is a forensics tool that functions as an EML file parser. If you've come across a suspicious email, you can employ this tool to swiftly extract pertinent information from the sender. Python, known for its user-friendly syntax, underlies this tool, ensuring the code is straightforward and highly adaptable.
            """
        )
        st.write("[Github Repository](https://github.com/JLowborn/kain-python)")

with st.container():    # Flask PyMongo API
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_github)
    with text_column:
        st.subheader("Flask & PyMongo API")
        st.write(
            """
            Here's a simple REST API built with Flask and MongoDB, designed for performing basic CRUD operations. I had the pleasure of showcasing this project during my secure development classes in college.
            """
        )
        st.write("[Github Repository](https://github.com/JLowborn/Flask-API)")

with st.container():    # Dice Password Generator
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_dice)
    with text_column:
        st.subheader("Dice Password Generator")
        st.write(
            """
            Introducing a straightforward password generator that utilizes the Electronic Frontier Foundation (EFF) passphrase method. This is an excellent way to create robust passwords that are also easy to remember. 
            """
        )
        st.write("[Github Repository](https://github.com/JLowborn/Dice-Password-Generator)")

# --- CONTACT ---
with st.container():
    st.write("#")
    st.header("Reach Me Out")
    st.write("######")
    left_column, right_column = st.columns(2)
    with left_column:
        load_view("views/contact.html")
    with right_column:
        st.empty()