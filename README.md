# 🛰️ VectoPulse - Behavioral Intelligence & Forensic Stylometry  ![Status: Prototype](https://img.shields.io/badge/Status-Prototype-blue?style=flat-square) ![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

## Overview
**VectoPulse** is a proof-of-concept **behavioral intelligence & forensic stylometry engine** built for OSINT analysts. It helps correlate anonymous or pseudonymous text to identify **mass misinformants, sock puppets, coordinated personas, and cross-platform actors** by analyzing *how* someone writes — not what they say. IPs can be spoofed. Accounts can be burned. VPNs are cheap. **Typing behavior is not.**

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
streamlit run vectopulse.py
# if you are on windows use:
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

## Methodology & AI Detection
VectoPulse analyzes *how* a text is written rather than *what* is written. This allows analysts to detect behavioral patterns, cross-platform personas, coordinated accounts, and potential AI-generated content.

### 1. Cognitive Complexity Analysis (Shannon Entropy)
- Measures unpredictability of character sequences.
- Formula used:
  \[
  H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)
  \]
  where \(P(x_i)\) is the probability of character \(x_i\) in the text.
- Human text shows unique entropy patterns.
- AI text often has smoother, more uniform entropy.

### 2. Structural DNA Mapping (Trigram Overlap)
- Breaks text into 3-character sequences (trigrams).
- Overlap score calculated as:
  \[
  Trigram\_Similarity(A,B) = \frac{|Trigrams(A) \cap Trigrams(B)|}{|Trigrams(A) \cup Trigrams(B)|}
  \]
- Humans exhibit repeated unconscious structures; AI tends to be more uniform.

### 3. Punctuation Rhythm Profiling
- Analyzes frequency and placement of punctuation marks.
- Rhythm similarity computed as normalized frequency difference for each punctuation:
  \[
  PR\_Similarity = 1 - \frac{|Freq_A - Freq_B|}{max(Freq_A, Freq_B)}
  \]
- Humans have subconscious punctuation habits.
- AI may use overly consistent or "correct" punctuation.

### 4. Multilingual Analysis
- Works across EN, SQ, DE, AR, ZH.
- Adjusts trigram and entropy calculations per language.
- Non-Latin scripts may have lower absolute similarity scores.

### 5. Similarity Index (SI)
- Aggregates entropy, trigram overlap, and punctuation rhythm into a single score:
  \[
  SI = w_1*Entropy\_Similarity + w_2*Trigram\_Similarity + w_3*PR\_Similarity
  \]
  where \(w_1, w_2, w_3\) are weighting coefficients.
- Provides a **directional probability** of behavioral similarity.
- Not a confirmation of identity.

### 6. AI vs Human Signals
- Human: uneven punctuation, unique sentence lengths, idiosyncratic trigram patterns.
- AI: uniform punctuation, consistent sentence length, smooth entropy.
- VectoPulse can indicate **possible AI-generated or heavily templated text**.

### 7. Offline Processing
- All processing is done locally.
- No text leaves your machine.

### 8. Workflow Summary
1. Input Reference Text (A) and Suspect Text (B).
2. Compute entropy, trigrams, and punctuation rhythm.
3. Output Similarity Index (SI).
4. Analyst interprets directional signal for cross-platform linkage, coordinated activity, or AI text detection.

---

## Testing & Accuracy (PoC)
- Validated as a **behavioral correlation PoC**, not an attribution engine.
- Tested across **5 languages** with controlled cases.
- Same-author samples consistently score **higher similarity**.
- Works best with:
  - Medium-to-long texts
  - Informal writing
  - Repeated human interaction (comments, replies, forum posts)

### Known Limitations
- Short texts reduce signal strength.
- Topic overlap can inflate similarity.
- Similarity Index values **not comparable across languages**.

---

## Example OSINT Use Cases
### Case 1 — Mass Misinformant Across Platforms
- Matches punctuation rhythms, entropy, and trigrams.
- Indicates potential cross-platform linkage.

### Case 2 — Coordinated Comment Network
- Reveals repeated linguistic micro-patterns.
- Suggests single operator or coordinated group.

### Case 3 — Forum Persona Reuse
- Detects structural DNA similarity and cognitive complexity.
- Supports persona continuity hypothesis.

---

### PoC - VectoPulse Action


<img width="1801" height="822" alt="image" src="https://github.com/user-attachments/assets/dc772291-45ca-4421-9c69-8894f27106b3" />

<img width="1801" height="822" alt="image" src="https://github.com/user-attachments/assets/9c2dff99-eb80-4cce-9eea-254e08986762" />

<img width="1801" height="822" alt="image" src="https://github.com/user-attachments/assets/dd8282e6-d1a0-4574-8ce6-7414d509c9ba" />


## Case Study and Inspiration for the tool — The Unabomber Writings
VectoPulse can illustrate **behavioral correlation in real investigations** using historical cases like Ted Kaczynski (the Unabomber):

**Scenario:**
- **Reference Text (A):** Kaczynski’s manifesto and known letters
- **Suspect Text (B):** Anonymous letters of unknown origin

**Step 1 — Cognitive Complexity (Entropy)**
- Compute Shannon entropy of character distributions in both texts.
- High similarity indicates comparable cognitive complexity and writing style.

**Step 2 — Structural DNA Mapping (Trigram Overlap)**
- Extract 3-character sequences (trigrams) from both texts.
- Compute overlap using:
  \[
  Trigram\_Similarity(A,B) = \frac{|Trigrams(A) \cap Trigrams(B)|}{|Trigrams(A) \cup Trigrams(B)|}
  \]
- Identifies repeated micro-patterns unique to the author.

**Step 3 — Punctuation Rhythm Profiling**
- Analyze punctuation frequency and placement using:
  \[
  PR\_Similarity = 1 - \frac{|Freq_A - Freq_B|}{max(Freq_A,Freq_B)}
  \]
- Detects subconscious punctuation habits, e.g., dashes, semicolons, commas.

**Step 4 — Combined Similarity Index**
- Weighted aggregation of entropy, trigram, and punctuation similarities:
  \[
  SI = w_1*Entropy\_Similarity + w_2*Trigram\_Similarity + w_3*PR\_Similarity
  \]
- High SI suggests strong behavioral similarity between the texts.

**Interpretation:**
- Directional evidence supports the hypothesis that both texts may have been written by the same individual.
- **Note:** SI is a probabilistic indicator, not definitive proof.

**Disclaimer:**
- Used here for educational and illustrative purposes.
- VectoPulse complements other forensic evidence but does not replace legal or investigative procedures.


## Contribution
- Open research PoC
- Contributions welcome for:
  - Additional behavioral signals
  - Language-specific normalization
  - Adversarial testing & evaluation

---

## License
MIT License — see LICENSE file.

---

## Developer
Korab Keqekolla // KING KOBRA II
