import streamlit as st
import re
import math
import html
import unicodedata
from collections import Counter

# --- SYSTEM CONFIGURATION ---
st.set_page_config(page_title="VectoPulse OSINT", page_icon="🛰️", layout="wide")
MAX_CHARS = 50000

# --- THE SOUL OF UI/UX: HIGH-CONTRAST TERMINAL & FIXED TOOLTIPS ---
st.markdown(f"""
    <style>
    .stApp {{ 
        background-color: #000000; 
        color: #FFFFFF; 
        font-family: 'Consolas', 'Monaco', monospace; 
    }}
    .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, 
    label[data-testid="stWidgetLabel"] p, div[data-testid="stMetricValue"] > div {{ 
        color: #FFFFFF !important; 
    }}
    .stTextArea textarea {{ 
        background-color: #0f172a !important; 
        color: #FFFFFF !important; 
        border: 2px solid #38bdf8 !important; 
        border-radius: 8px; 
        font-size: 1.1rem !important;
    }}
    div[data-testid="stTooltipContent"] {{
        background-color: #1e293b !important;
        color: #FFFFFF !important;
        border: 1px solid #38bdf8 !important;
    }}
    .stTooltipIcon {{ color: #38bdf8 !important; }}
    div[data-testid="stMetric"] {{ 
        background-color: #111827; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #38bdf8;
    }}
    div[data-testid="stMetricLabel"] {{ color: #38bdf8 !important; font-weight: bold !important; }}
    .dna-chip {{ 
        background-color: #0f172a; 
        padding: 6px 14px; 
        border-radius: 4px; 
        color: #38bdf8; 
        border: 1px solid #38bdf8; 
        margin: 5px; 
        display: inline-block;
        font-weight: bold;
    }}
    .stButton button {{ 
        background: linear-gradient(135deg, #38bdf8 0%, #1d4ed8 100%); 
        color: #FFFFFF !important; 
        border: none; 
        padding: 18px; 
        font-weight: 900 !important; 
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 3px;
    }}
    .footer {{ 
        margin-top: 60px; width: 100%; 
        background-color: #000000; color: #38bdf8; 
        text-align: center; padding: 25px; 
        border-top: 1px solid #1e293b; 
    }}
    .disclaimer {{ font-size: 0.75rem; color: #64748b; margin-top: 10px; }}
    </style>
    """, unsafe_allow_html=True)

# --- ANALYTICAL ENGINES ---
@st.cache_data
def analyze_text(text):
    if not text: return 0, 0, Counter()
    
    # Career-Saver 1: Unicode Normalization (Prevents hidden character exploits)
    text = unicodedata.normalize('NFKC', text)
    text = text[:MAX_CHARS]
    
    chars = [c for c in text.lower() if not c.isspace()]
    symbols = re.findall(r'[^\w\s]', text)
    if not chars: return 0, 0, Counter()
    
    # Advanced Entropy (Normalized against 8-bit or Logographic scale)
    counts = Counter(chars)
    total = len(chars)
    raw_entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    
    # Career-Saver 2: Adaptive Scaling (Prevents entropy score blowing out in non-Latin scripts)
    scaling_factor = 8.0 if any(ord(c) < 128 for c in chars) else 12.0
    norm_entropy = min(raw_entropy / scaling_factor, 1.0) 
    
    punc_ratio = len(symbols) / total if total > 0 else 0
    trigrams = [text.lower()[i:i+3] for i in range(len(text)-2)]
    return norm_entropy, punc_ratio, Counter(trigrams)

def calculate_cosine_sim(c1, c2):
    terms = set(c1).union(c2)
    dot_product = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    mag1 = math.sqrt(sum(v**2 for v in c1.values()))
    mag2 = math.sqrt(sum(v**2 for v in c2.values()))
    return dot_product / (mag1 * mag2) if (mag1 * mag2) else 0

def sanitize_chip(val):
    return f'<span class="dna-chip">{html.escape(val)}</span>'

# --- HEADER ---
st.title("🛰️ VectoPulse: Behavioral Intelligence")
st.caption("`SYSTEM: ONLINE` | `VERSION: 3.2-ELITE` | `PROTOCOL: HEURISTIC_STYLO`")

# --- ORIGINAL MISSION BRIEFING ---
with st.expander("📂 MISSION BRIEFING & METHODOLOGY (READ BEFORE USE)", expanded=True):
    col_a, col_b = st.columns([1.5, 1])
    with col_a:
        st.markdown("### 🕵️‍♂️ Operational Protocol")
        st.write("""
        **VectoPulse** is a specialized engine designed to correlate the **'Linguistic Fingerprint'** of anonymous targets. 
        While IP addresses and metadata can be spoofed, humans are creatures of habit. 
        A target's unique syntax, complexity, and character-level DNA are nearly impossible to mask consistently.
        
        **The Core Logic:**
        1. **Cognitive Complexity:** Analyzes Shannon Entropy to detect the unique 'chaos' of a user's mind.
        2. **N-Gram DNA:** Maps 3-character sequences to identify shared structural habits.
        3. **Punctuation Density:** Tracks subconscious symbol usage patterns.
        
        **Calculation:** Final SI is a weighted average: 50% Trigrams, 30% Entropy, 20% Punc Density.
        """)
    with col_b:
        st.markdown("### 📊 Similarity Index (SI)")
        st.info("**> 85%:** 🔴 **CRITICAL** (Same Author) | **60-84%:** 🟠 **PROBABLE** | **< 60%:** 🟢 **LOW**")

st.divider()

# --- INPUT SECTORS ---
c1, c2 = st.columns(2)
with c1:
    st.markdown("### 📂 Input Logs A (Reference)")
    text_a = st.text_area("Known or suspected source material", height=280, placeholder="[PASTE TARGET DATA HERE]", key="a")
with c2:
    st.markdown("### 📂 Input Logs B (Suspect)")
    text_b = st.text_area("Material from suspect profile", height=280, placeholder="[PASTE SUSPECT DATA HERE]", key="b")

# --- EXECUTION ---
if st.button("🚀 INITIATE BEHAVIORAL CORRELATION"):
    if text_a and text_b:
        with st.spinner("RUNNING FORENSIC DNA SCAN..."):
            ent_a, punc_a, counts_a = analyze_text(text_a)
            ent_b, punc_b, counts_b = analyze_text(text_b)
            
            ngram_sim = calculate_cosine_sim(counts_a, counts_b)
            comp_sim = 1 - abs(ent_a - ent_b)
            punc_sim = 1 - abs(punc_a - punc_b)
            
            si_score = (ngram_sim * 0.5) + (comp_sim * 0.3) + (punc_sim * 0.2)
            if len(text_a) < 150 or len(text_b) < 150: si_score -= 0.10
            si_score = max(0, min(si_score, 1))

            st.divider()
            st.markdown("## 📡 FORENSIC ANALYSIS REPORT")
            m1, m2, m3, m4 = st.columns(4)
            
            m1.metric("Similarity Index", f"{si_score*100:.1f}%", help="Final weighted overlap.")
            m2.metric("Punc Match", f"{punc_sim*100:.1f}%", help="Subconscious rhythm of symbol usage.")
            m3.metric("Alpha Entropy", f"{ent_a:.2f}", help="Complexity score for Target Alpha.")
            m4.metric("Bravo Entropy", f"{ent_b:.2f}", help="Complexity score for Target Bravo.")

            st.markdown("#### 🧬 Shared Structural DNA (Common Trigrams)")
            shared = [item for item, count in (counts_a & counts_b).most_common(15)]
            if shared:
                html_chips = "".join([sanitize_chip(x) for x in shared])
                st.markdown(html_chips, unsafe_allow_html=True)

st.divider()

# --- CASE STUDY & OSINT SECTION ---
st.markdown("### 📜 Forensic Case Study & OSINT Context")
col_story, col_osint = st.columns(2)

with col_story:
    st.markdown("#### ⚖️ The Unabomber Precedent")
    st.write("""
    For decades, the FBI could not identify the Unabomber via technical evidence. Success came when forensic linguist James Fitzgerald recognized unique patterns in the Manifesto matching Ted Kaczynski's personal letters. This tool automates that same structural DNA analysis.
    """)

with col_osint:
    st.markdown("#### 🛰️ Unmasking Sock Puppets & Informants")
    st.write("""
    This behavioral engine is designed to unmask **Sock Puppets** and **Mass-Informants** across different platforms. Even if a target hides their IP, they cannot hide their **Punctuation Rhythms** and **Structural DNA**—the permanent fingerprints of identity.
    """)

st.markdown("""
    <div class="footer">
        DEVELOPED FROM KORAB KEQEKOLLA // KING KOBRA II WITH LOVE
        <div class="disclaimer">LEGAL DISCLAIMER: RESULTS ARE PROBABILISTIC / SUGGESTIVE. NOT ADMISSIBLE AS PROOF.</div>
    </div>
    """, unsafe_allow_html=True)