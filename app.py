!pip install streamlit
%%writefile birthday_gift.py
import streamlit as st

# Page configuration
st.set_page_config(page_title="Happy Birthday! ❤️", page_icon="🎂", layout="centered")

# Cute Yellow Stripes Background & Pink Buttons CSS
st.markdown("""
    <style>
    .stApp {
        background: repeating-linear-gradient(
          90deg,
          #FFFDF0,
          #FFFDF0 20px,
          #FFF3CD 20px,
          #FFF3CD 40px
        );
    }
    div.stButton > button:first-child {
        background-color: #FFB3B3;
        color: white;
        border-radius: 20px;
        border: 2px solid #FFA0A0;
        padding: 10px 24px;
        font-weight: bold;
    }
    h1, h2, h3, h4, p, span, div {
        color: #4A154B !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# State management for pages
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# --- PAGE 1: ACTUAL PASSWORD LOGIN ---
if st.session_state.page == 'login':
    st.write("### Verification Required 🔒")
    password = st.text_input("Enter the password to view:", type="password")
    captcha = st.checkbox("I am not a robot 🤖")
    
    if st.button("Continue"):
        if password == "Tillu Bhai" and captcha:
            st.session_state.page = 'challenge'
            st.rerun()
        elif not captcha:
            st.warning("Please check the captcha first!")
        else:
            st.error("Incorrect Password! Hint: It's the name which I love to call you 😉")

# --- PAGE 2: THE YES/NO CHALLENGE ---
elif st.session_state.page == 'challenge':
    st.write("### Hey! I made something for you, do you wanna see it? 🐶")
    st.image(r"C:\Users\jaski\Downloads\WhatsApp Image 2026-08-04 at 23.52.00.jpeg")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 😍"):
            st.session_state.page = 'dashboard'
            st.rerun()
    with col2:
        if st.button("No 😜"):
            st.session_state.page = 'sad_page'
            st.rerun()

# --- PAGE 3: FUNNY SAD PAGE ---
elif st.session_state.page == 'sad_page':
    st.write("### SERIOUSLY!? How dare you... hmph! 😡")
    st.image(r"C:\Users\jaski\Downloads\WhatsApp Image 2026-08-04 at 23.52.01.jpeg")
    if st.button("Go Back ↩️"):
        st.session_state.page = 'challenge'
        st.rerun()

# --- PAGE 4: MAIN DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.write("## ✨ Click on each item to open ✨")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("📷 *Memories*")
        if st.button("Open Camera"):
            st.session_state.page = 'memories'
            st.rerun()
            
    with col2:
        st.write("✉️ *Letter*")
        if st.button("Read Message"):
            st.session_state.page = 'letter'
            st.rerun()
            
    with col3:
        st.write("🎵 *Our Song*")
        st.link_button("Play Music", "https://youtu.be/W1PaMD9GmCc?si=E0FwOl-TDOu7O3wm")

# --- PAGE 5: MEMORIES PHOTO GALLERY ---
elif st.session_state.page == 'memories':
    st.write("### Moments of us ❤️")
    st.image([
    r"C:\Users\jaski\OneDrive\Pictures\tt.jpeg",
    r"C:\Users\jaski\OneDrive\Pictures\WhatsApp Image 2026-10-04 at 23.18.54.jpeg"
], caption=["Best Memories", "Best Bhaiii"], width=250)
    if st.button("Back to Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()

# --- PAGE 6: BIRTHDAY LETTER ---
elif st.session_state.page == 'letter':
    st.write("### Happy Birthday, Tillu Bhaii! 📝")
    st.info("Tiilu Bhaii dekho!! yha mujhse bda sa paragraph to nhi likha jayega vo emoji vgera lga kr but jo likhungi smjh aa jayega utna kafi hai mere liye to tu na bohot strong hai bss apne aap pr trust rkh and Self love kr ...")
    if st.button("Back to Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()

!streamlit run birthday_gift.py
 
