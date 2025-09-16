import streamlit as st
import time
from pathlib import Path
import base64

# ===============================
# 🎁 CONFIG — personalize here
# ===============================
CONFIG = {
    "recipient_name": "RAJ",
    "message": "Wishing you joy, health, and all the happiness in the world. Happy Birthday! 💖",
    "photo_path": "assets/recipient.jpg",
    "audio_path": "assets/birthday.mp3",
}

# ===============================
# 🌙 Page Settings
# ===============================
st.set_page_config(
    page_title=f"Happy Birthday {CONFIG['recipient_name']}! 🎂",
    page_icon="🎂",
    layout="centered",
)

# ===============================
# 🌗 Dark / Light Mode Toggle
# ===============================
dark = st.toggle("🌙 Dark Mode", value=True)
if dark:
    st.markdown(
        "<style>body, .stApp{background:#111;color:#eee;}</style>",
        unsafe_allow_html=True,
    )

# ===============================
# ✨ CSS Animations (balloons/confetti only)
# ===============================
st.markdown("""
<style>
.fade-in {
    animation: fadeIn 2.5s ease-in-out forwards;
    opacity: 0;
}
@keyframes fadeIn { to {opacity: 1;} }

.balloons {
  position: fixed; top: 100%; width: 100%;
  z-index: 9999; pointer-events: none;
}
.balloon {
  position: absolute; bottom: -150px; width: 50px; height: 70px;
  background: #ff4b5c; border-radius: 50% 50% 45% 45%;
  animation: float 8s ease-in infinite;
}
.balloon:after {
  content: ''; position: absolute; bottom: -20px; left: 50%;
  width: 2px; height: 20px; background: #555;
}
@keyframes float {
  0% {transform: translateY(0);}
  100% {transform: translateY(-120vh);}
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 📸 Show recipient photo (static)
# ===============================
if Path(CONFIG["photo_path"]).exists():
    st.image(CONFIG["photo_path"], width=250, caption="", use_container_width=False)
else:
    st.warning("Photo not found. Please place recipient.jpg inside assets/")

# ===============================
# 🎵 Background music autoplay
# ===============================
if Path(CONFIG["audio_path"]).exists():
    with open(CONFIG["audio_path"], "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

# ===============================
# 🎈 Balloons + Confetti
# ===============================
st.markdown("""
<div class='balloons'>
  <div class='balloon' style='left:10%'></div>
  <div class='balloon' style='left:30%;background:#ffcc00;animation-delay:1s;'></div>
  <div class='balloon' style='left:50%;background:#4b9cff;animation-delay:2s;'></div>
  <div class='balloon' style='left:70%;background:#8aff4b;animation-delay:3s;'></div>
  <div class='balloon' style='left:90%;background:#ff8aff;animation-delay:4s;'></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
setTimeout(()=>{
  confetti({ particleCount: 200, spread: 100, origin: { y: 0.7 } });
}, 500);
</script>
""", unsafe_allow_html=True)

# ===============================
# 🌳 Tree → Heart Animation
# ===============================
def celebration_animation():
    placeholder = st.empty()
    for i in range(4):
        placeholder.markdown("<h1 style='text-align:center;font-size:90px;'>🌳</h1>", unsafe_allow_html=True)
        time.sleep(0.25)
        placeholder.markdown("<h1 style='text-align:center;font-size:90px;'>❤️</h1>", unsafe_allow_html=True)
        time.sleep(0.25)
    placeholder.empty()

celebration_animation()

# ===============================
# 💌 Final Birthday Message
# ===============================
st.markdown(
    f"<h1 class='fade-in' style='text-align:center;'>🎂 Happy Birthday {CONFIG['recipient_name']}! 🎂</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p class='fade-in' style='font-size:22px;text-align:center;'>{CONFIG['message']}</p>",
    unsafe_allow_html=True,
)

# ===============================
# 🔁 Replay Celebration
# ===============================
if st.button("🔁 Replay Celebration"):
    celebration_animation()
