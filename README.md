# The Wayfarer's Scroll: Native Scripture in Dark-Fantasy Games

Built for the **Scripture in New Frontiers** hackathon. A responsive, atmospheric dark-fantasy visual novel prototype engineered to bring sacred wisdom directly into modern interactive gaming loops.

## 🔗 Project Links
* **Live Deployment:** [Play the Game Here](https://the-wayfarers-scroll-ibset4cqgqrkbnnjmumwqu.streamlit.app/)

---

## 🌌 The Vision
Millions of players spend hours immersed in dark-fantasy roguelikes and RPGs, yet faith and scripture are completely absent from these virtual landscapes. **The Wayfarer's Scroll** bridges this gap. Instead of breaking player immersion with forced popups, this framework weaves Scripture directly into the core gameplay survival mechanics. 

Players navigate a gritty world where their choices drain their structural spirit pool. When their resolve breaks, unrolling a holy scripture scroll is the only lifeline available to restore their character and survive the journey.

---

## 🎨 Custom Art & Photoshop Design
To build a high-stakes, atmospheric environment, all character states were custom-designed and edited inside **Photoshop**. 
* Dynamic visual profiles were created to mirror the player's statistical health loop in real-time.
* Character assets transition cleanly between **Resolved**, **Fading**, and **Game Over** visual states based on active spirit metrics.
* Fine-tuned lighting, gritty textures, and deep shadow adjustments ensure the aesthetic aligns with premium dark-fantasy indie standards.

---

## 🛠️ Architecture & Core Mechanics
The prototype is written entirely in **Python** and structured as a responsive single-page web architecture:
* **Narrative Engine:** Generates environmental high-stakes dilemmas (blinding fogs, psychological threats, broken pathways) that dynamically tax the player's character state.
* **Scripture System:** Functions as the mechanical engine core. When player stats collapse to critical thresholds, the application triggers a framework request that pulls targeted verses focused on strength, resilience, and faith renewal. Reading the text updates the UI and replenishes the player's attributes.
* **Layout Optimization:** Leverages custom CSS injections to cleanly lock the character portraits, action runes, audio components, and structural statistics into a sleek, zero-scroll single-viewport presentation.

---

## 🚀 Getting Started Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
