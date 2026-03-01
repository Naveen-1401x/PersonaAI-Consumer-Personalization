# PersonaAI – Real-Time Consumer Personalization Engine

## Overview
PersonaAI is an AI-powered real-time personalization engine designed to enhance digital consumer experiences using behavioral clustering and dynamic UI adaptation.

Unlike traditional systems that rely solely on past purchase history, PersonaAI analyzes live behavioral signals such as browsing duration, click frequency, and spending patterns to dynamically classify users into behavioral personas.

Based on persona classification, the system adapts interface layout, recommendations, and promotional strategies in real time.

---

## Problem Statement
Current personalization systems are largely static and history-based. They fail to adapt to real-time user behavior, resulting in:

- Generic user experiences
- Irrelevant recommendations
- Decision fatigue
- Reduced engagement and conversions

---

## Proposed Solution
PersonaAI introduces a behavioral intelligence layer that:

1. Collects user interaction metrics
2. Applies KMeans clustering
3. Assigns dynamic persona labels
4. Adapts UI and recommendation logic
5. Continuously updates personalization based on new interactions

---

## Tech Stack
- Python
- Scikit-learn (KMeans)
- FastAPI
- React.js (UI mock)
- MongoDB
- AMD Accelerated Compute (Conceptual Integration)

---

## Architecture Flow
User Interaction → Data Collection → Preprocessing → Clustering Model → Persona Assignment → Dynamic UI Adaptation → Feedback Loop

---

## Usage of AMD Technology
PersonaAI can leverage AMD high-performance processors and GPUs to accelerate:

- Real-time clustering computation
- Low-latency model inference
- Parallel behavioral analytics
- Scalable deployment for consumer platforms

---

## Future Scope
- Real-time streaming data integration
- Edge deployment using AMD acceleration
- SaaS-based personalization engine
- Integration with e-commerce and OTT platforms

---

## Repository Structure
- model/ → Clustering logic
- dataset/ → Sample behavioral data
- docs/ → PPT and architecture diagrams

---

## Prototype Assets

PPT Deck: [View Presentation](./docs/PersonaAI_AMD_Slingshot_Prototype.pdf)
