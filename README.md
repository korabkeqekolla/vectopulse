# 🛰️ VectoPulse - Behavioral Intelligence & Forensic Stylometry

![Status: Prototype](https://img.shields.io/badge/Status-Prototype-blue?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

## Overview
**VectoPulse** is a proof-of-concept **behavioral intelligence & forensic stylometry engine** built for OSINT analysts.

It helps correlate anonymous or pseudonymous text to identify **mass misinformants, sock puppets, coordinated personas, and cross-platform actors** by analyzing *how* someone writes — not what they say.

IPs can be spoofed. Accounts can be burned. VPNs are cheap.
**Typing behavior is not.**

> **Disclaimer:** VectoPulse produces **probabilistic similarity signals**, not identity confirmation. Results are suggestive and must never be treated as proof.

---

## Features

- 🧠 **Cognitive Complexity Analysis** (character-level Shannon entropy)
- 🧬 **Structural DNA Mapping** via trigram overlap
- ✒️ **Punctuation Rhythm Profiling** (subconscious symbol usage)
- 🌍 **Multilingual by Design** (tested with EN, SQ, DE, AR, ZH)
- 🖥️ High-contrast, analyst-friendly Streamlit UI
- 🔒 Offline processing — no data exfiltration

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/korabkeqekolla/vectopulse.git
cd vectopulse

# 2. Install dependencies
pip install -r requirements.txt

```

---

## Usage

1. Launch the application:
```bash
streamlit run vectopulse.py // if you are on windows use
python -m streamlit run vectopulse.py
```

2. Paste **Reference Text (A)** and **Suspect Text (B)** from any source:
   - Forums
   - Comment sections
   - Paste sites
   - Social media posts

3. Run **Behavioral Correlation** to receive:
   - Similarity Index (SI)
   - Entropy comparison
   - Punctuation alignment
   - Shared structural trigrams

> ⚠️ SI scores are **directional indicators**, not identity proof.

---

## Testing & Accuracy (PoC)

VectoPulse was validated as a **behavioral correlation PoC**, not an attribution engine.

- Tested across **5 languages** with multiple controlled cases
- Same-author samples consistently score **higher similarity** than different-author samples
- Best performance with:
  - Medium-to-long texts
  - Natural, informal writing
  - Repeated human interaction (comments, replies, forum posts)

### Known Limitations
- Short texts reduce signal strength
- Topic overlap can inflate similarity
- Non-Latin scripts (e.g. Chinese, Arabic) show lower absolute scores
- Similarity Index values are **not comparable across languages**

---

## Example OSINT Use Cases

### Case 1 — Mass Misinformant Across Platforms
A highly active "security expert" on a hacking forum spreads technical misinformation.
A suspected social media account pushes the *same narratives* under a different identity.

VectoPulse highlights:
- Matching punctuation rhythms
- Similar entropy profiles
- Overlapping trigram DNA

➡️ Analyst gains **strong directional signal** for cross-platform linkage.

---

### Case 2 — Coordinated Comment Network
Multiple accounts comment under cybersecurity news articles, appearing independent.

Behavioral correlation reveals:
- Near-identical structural habits
- Consistent symbol usage
- Repeated linguistic micro-patterns

➡️ Indicates **single operator or tightly coordinated group**.

---

### Case 3 — Forum Persona Reuse
An old forum account disappears after exposure.
A new account emerges months later with a different username.

VectoPulse detects:
- Shared structural DNA
- Similar cognitive complexity

➡️ Supports **persona continuity hypothesis**.

---

## Contribution

This project is released as an **open research PoC**

Contributions are welcome for:
- Additional behavioral signals
- Language-specific normalization
- Adversarial testing & evaluation

---

## License
MIT License — see LICENSE file.

---

## Developer
Korab Keqekolla // KING KOBRA II
---
