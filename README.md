# Spotify Content Evaluation System

## Project Overview

This project simulates a Spotify-style content understanding and evaluation system.

The system combines:

- Content taxonomy design
- Human annotation workflows
- Machine learning model evaluation
- User engagement analytics

The goal is to evaluate how accurately content can be classified and how model predictions relate to user behaviour signals.

---

## Dataset

The dataset contains 500 synthetic content items.

Content categories:

- Music
- Podcast
- Audiobook
- Mixed

Features include:

- Content metadata
- Human labels
- Model predictions
- Confidence scores
- User engagement metrics

---

## Evaluation Metrics

### Model Accuracy

Model A Accuracy: 28.6%

Model B Accuracy: 25.4%

Model A outperformed Model B by 3.2 percentage points.

### Human–Model Agreement

Agreement Rate: 28.6%

Disagreement Rate: 71.4%

### Confidence Calibration

Overconfident Error Rate: 6.2%

### Engagement Analysis

Content engagement ranking:

1. Music (0.540)
2. Mixed (0.481)
3. Audiobook (0.474)
4. Podcast (0.398)

---

## Key Findings

- Model A performed better than Model B.
- Audiobooks were the most difficult content type to classify.
- Podcasts achieved the highest completion rates.
- Music achieved the highest overall engagement score.
- Model confidence was not always aligned with prediction correctness.

---

## Skills Demonstrated

- Python
- Pandas
- Data Analysis
- Machine Learning Evaluation
- Content Taxonomy Design
- Annotation System Evaluation
- Product Analytics
  ## How to Run This Project

Install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn

Go to project folder:

cd ~/Desktop/spotify_project

Run dataset generator:

python3 src/generate_dataset.py

Run analysis:

python3 src/evaluation_engine.py
