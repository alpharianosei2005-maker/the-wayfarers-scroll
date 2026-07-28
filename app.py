import streamlit as st
import random
import os

# ==========================================
# 🎨 CUSTOM STYLE PACK & CONTENT MAPPING
# ==========================================
st.set_page_config(page_title="The Wayfarer's Scroll", page_icon="📜", layout="wide")

st.markdown("""
    <style>
    /* Dark Fantasy Stone Texture Base */
    .stApp {
        background: linear-gradient(rgba(13, 15, 18, 0.9), rgba(20, 24, 30, 0.97)), 
                    url('https://www.transparenttextures.com/patterns/dark-matter.png');
        color: #e2d4b7;
        font-family: 'Georgia', serif;
    }
    
    /* Strict Card Sizing Bound (Keeps Shaddie and Elara Identical) */
    .character-card img, .selection-card img {
        max-height: 420px !important;
        object-fit: contain !important;
        width: auto !important;
        margin: 0 auto !important;
        display: block;
        border-radius: 6px;
    }
    
    /* Elegant Title Framing */
    .game-title {
        text-align: center;
        font-size: 2.8rem;
        color: #d4af37;
        text-shadow: 0px 0px 18px rgba(212, 175, 55, 0.5);
        font-weight: bold;
        margin-bottom: 2px;
        font-family: 'Times New Roman', serif;
    }
    .game-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #8c7d63;
        font-style: italic;
        margin-bottom: 20px;
    }

    /* Immersive Visual Novel Containers */
    .story-box {
        background-color: rgba(22, 26, 34, 0.85);
        padding: 30px;
        border-radius: 6px;
        border-left: 4px solid #d4af37;
        margin-bottom: 20px;
        font-size: 20px;
        line-height: 1.6;
        color: #e0e6ed;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
    }
    .scroll-box {
        background-color: rgba(28, 20, 14, 0.9);
        padding: 20px;
        border-radius: 6px;
        border: 1px dashed #ff9933;
        margin-bottom: 20px;
        color: #ffcc66;
        font-style: italic;
        font-size: 18px;
    }
    .stat-text {
        font-family: 'Courier New', monospace;
        font-size: 18px;
        font-weight: bold;
        color: #c5b493;
        margin-bottom: 6px;
    }
    
    /* Interactive Button Matrix */
    .stButton>button {
        background-color: #161a22; 
        color: #d4af37; 
        border: 1px solid #4a3b2c; 
        border-radius: 4px;
        padding: 14px 20px; 
        font-weight: bold; 
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #d4af37; 
        color: #0d0f12; 
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
    }
    
    /* Absolute Layout Destruction for Streamlit Audio Element Widgets */
    iframe, audio, div[data-testid="stAudio"], .element-container:has(audio) {
        display: none !important;
        height: 0px !important;
        position: absolute !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 📊 GAME STATE INTERFACES
# ==========================================
if "screen" not in st.session_state:
    st.session_state.screen = "menu"  
if "chosen_character" not in st.session_state:
    st.session_state.chosen_character = None  
if "spirit" not in st.session_state:
    st.session_state.spirit = 100
if "steps" not in st.session_state:
    st.session_state.steps = 0
if "current_scene_text" not in st.session_state:
    st.session_state.current_scene_text = "The frontier stretches forward into the unknown. Your quest to deliver the broken kingdom's final embers begins now. Every choice tests your spiritual resolve."
if "active_scroll" not in st.session_state:
    st.session_state.active_scroll = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "play_sound" not in st.session_state:
    st.session_state.play_sound = None

# ==========================================
# 🔊 AUDIO HOOK CONTROLLER
# ==========================================
def trigger_audio(sound_key):
    st.session_state.play_sound = sound_key

if st.session_state.play_sound == "walk" and os.path.exists("step.mp3"):
    st.audio("step.mp3", autoplay=True) 
    st.toast("🐾 Trudging deeper across the boundary line...")
    st.session_state.play_sound = None
elif st.session_state.play_sound == "heal" and os.path.exists("restore.mp3"):
    st.audio("restore.mp3", autoplay=True)
    st.toast("✨ Vitality surges through the artifact...")
    st.session_state.play_sound = None
elif st.session_state.play_sound == "game_over" and os.path.exists("over.mp3"):
    st.audio("over.mp3", autoplay=True)
    st.toast("💀 The flame expires.")
    st.session_state.play_sound = None
elif st.session_state.play_sound == "restart" and os.path.exists("restart.mp3"):
    st.audio("restart.mp3", autoplay=True)
    st.toast("🌅 Chronology resets...")
    st.session_state.play_sound = None

# ==========================================
# 🛠️ ROGUELIKE MECHANICAL LOGIC ENGINE
# ==========================================
def call_gloo_ai_dilemma():
    dilemmas = [
        "You encounter a broken traveler resting heavily against the base of an ancient ironwood tree.",
        "A blindingly thick supernatural fog descends, clouding out all trace of landmarks.",
        "A rickety, splintered rope bridge looms ahead, swaying wildly over a massive canyon fissure.",
        "Vivid, malicious crimson eyes track your movements from the pitch-black hollow of a twisted oak tree.",
        "The main trail fragments directly into a fork, splitting into three ominous routes ahead."
    ]
    return random.choice(dilemmas)

def call_youversion_scripture():
    verses = [
        {"text": "He gives strength to the weary and increases the power of the weak.", "ref": "Isaiah 40:29"},
        {"text": "Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you.", "ref": "Isaiah 41:10"},
        {"text": "The Lord is my light and my salvation—whom shall I fear?", "ref": "Psalm 27:1"},
        {"text": "Be strong and courageous. Do not be afraid; do not be discouraged...", "ref": "Joshua 1:9"},
        {"text": "But those who hope in the Lord will renew their strength. They will soar on wings like eagles.", "ref": "Isaiah 40:31"}
    ]
    return random.choice(verses)

def handle_advance():
    st.session_state.steps += 1
    st.session_state.spirit -= 20
    st.session_state.active_scroll = None
    
    if st.session_state.spirit <= 0:
        st.session_state.spirit = 0
        st.session_state.game_over = True
        char_name = st.session_state.chosen_character.capitalize()
        st.session_state.current_scene_text = f"💀 {char_name}'s spirit has completely evaporated into the dark atmosphere. The frontier claims another soul."
        trigger_audio("game_over")
    else:
        text = call_gloo_ai_dilemma()
        st.session_state.current_scene_text = f"Step {st.session_state.steps}: {text}"
        trigger_audio("walk")

def handle_rest():
    verse_data = call_youversion_scripture()
    st.session_state.active_scroll = f'"{verse_data["text"]}" — {verse_data["ref"]}'
    st.session_state.spirit = min(100, st.session_state.spirit + 40)
    trigger_audio("heal")

def reset_game():
    st.session_state.screen = "menu"
    st.session_state.spirit = 100
    st.session_state.steps = 0
    st.session_state.current_scene_text = "The frontier stretches forward into the unknown. Your quest to deliver the broken kingdom's final embers begins now. Every choice tests your spiritual resolve."
    st.session_state.active_scroll = None
    st.session_state.game_over = False
    st.session_state.chosen_character = None
    trigger_audio("restart")

# ==========================================
# 🖥️ STAGE 1: ENTRY MENU GRAPHIC
# ==========================================
if st.session_state.screen == "menu":
    st.markdown('<div class="game-title">📜 THE WAYFARER\'S SCROLL</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-subtitle">A Mythic Dark-Fantasy Visual Novel Roguelike</div>', unsafe_allow_html=True)
    
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("UNROLL THE SCROLL", use_container_width=True):
            st.session_state.screen = "character_selection"
            st.rerun()

# ==========================================
# 👥 STAGE 2: IDENTITY BINDING MATRIX
# ==========================================
elif st.session_state.screen == "character_selection":
    st.markdown('<div class="game-title">CHOOSE YOUR SOUL ANCHOR</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-subtitle">Select a wayfarer to brave the deep timberlands</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 style='text-align: center;'>🇬🇭 SHADDIE</h3>", unsafe_allow_html=True)
        if os.path.exists("shaddie_resolved.png"):
            st.markdown('<div class="selection-card">', unsafe_allow_html=True)
            st.image("shaddie_resolved.png")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-style: italic; color: #8c7d63;'>Forged under fierce suns, bounded by ancestral iron protection.</p>", unsafe_allow_html=True)
        if st.button("Bind Shaddie's Fate", use_container_width=True):
            st.session_state.chosen_character = "shaddie"
            st.session_state.screen = "game"
            trigger_audio("restart")
            st.rerun()
            
    with col2:
        st.markdown("<h3 style='text-align: center;'>🇺🇸 ELARA</h3>", unsafe_allow_html=True)
        if os.path.exists("elara_resolved.png"):
            st.markdown('<div class="selection-card">', unsafe_allow_html=True)
            st.image("elara_resolved.png")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-style: italic; color: #8c7d63;'>Far from home, tracking paths illuminated by an undying artifact beacon.</p>", unsafe_allow_html=True)
        if st.button("Bind Elara's Fate", use_container_width=True):
            st.session_state.chosen_character = "elara"
            st.session_state.screen = "game"
            trigger_audio("restart")
            st.rerun()

# ==========================================
# ⚔️ STAGE 3: RUNTIME NARRATIVE WINDOW
# ==========================================
elif st.session_state.screen == "game":
    char = st.session_state.chosen_character
    
    if st.session_state.spirit <= 0:
        char_card = f"{char}_game_over.png"
    elif st.session_state.spirit <= 50:
        char_card = f"{char}_fading.png"
    else:
        char_card = f"{char}_resolved.png"
        
    flag = "🇬🇭" if char == "shaddie" else "🇺🇸"
    st.markdown(f'<div class="game-title">{flag} {char.upper()}\'S VOYAGE</div>', unsafe_allow_html=True)
    st.divider()

    left_panel, right_panel = st.columns([1, 2])

    # Left Screen Segment: Portrait Dynamic Containment Only
    with left_panel:
        st.markdown('<div class="character-card">', unsafe_allow_html=True)
        if os.path.exists(char_card):
            st.image(char_card)
        else:
            st.error(f"Asset Error: '{char_card}' not detected.")
        st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"<p class='stat-text'>👣 Traveled Distance: {st.session_state.steps} / 10 Leagues</p>", unsafe_allow_html=True)
        
        progress_percentage = min(1.0, st.session_state.steps / 10.0)
        st.progress(progress_percentage)
        
        if st.session_state.spirit > 50:
            st.success(f"💖 Structural Spirit: {st.session_state.spirit}%")
        elif st.session_state.spirit > 20:
            st.warning(f"⚠️ Spirit Dissipating: {st.session_state.spirit}%")
        else:
            st.error(f"🚨 Collapse Imminent: {st.session_state.spirit}%")

    # Right Screen Segment: pure Log Text Box, Wisdom Scrolls, and Actions
    with right_panel:
        st.markdown(f"<div class='story-box'><strong>Frontier Log:</strong><br/>{st.session_state.current_scene_text}</div>", unsafe_allow_html=True)
        
        if st.session_state.active_scroll:
            st.markdown(f"<div class='scroll-box'><b>📜 Opened Wisdom Scroll:</b><br/>{st.session_state.active_scroll}</div>", unsafe_allow_html=True)
            st.balloons()
            
        st.markdown("### ⚡ ACTION RUNES")
        btn_col1, btn_col2, btn_col3 = st.columns(3)
        
        with btn_col1:
            st.button("Venture Forward (-20 Spirit)", on_click=handle_advance, disabled=st.session_state.game_over, key="btn_adv")
        with btn_col2:
            st.button("Unroll Scripture Scroll (+40 Spirit)", on_click=handle_rest, disabled=st.session_state.game_over, key="btn_rst")
        with btn_col3:
            st.button("Restart Journey", on_click=reset_game, key="btn_back")