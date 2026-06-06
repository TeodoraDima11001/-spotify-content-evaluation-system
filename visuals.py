import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/content_dataset.csv")

# -----------------------------
# 1. MODEL ACCURACY COMPARISON
# -----------------------------

df["model_A_correct"] = df["model_A_prediction"] == df["content_type"]
df["model_B_correct"] = df["model_B_prediction"] == df["content_type"]

accuracy = {
    "Model A": df["model_A_correct"].mean(),
    "Model B": df["model_B_correct"].mean()
}

plt.figure()
plt.bar(accuracy.keys(), accuracy.values())
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# -----------------------------
# 2. ENGAGEMENT BY CONTENT TYPE
# -----------------------------

engagement = df.groupby("content_type")["completion_rate"].mean()

plt.figure()
engagement.plot(kind="bar")
plt.title("Engagement by Content Type")
plt.ylabel("Avg Completion Rate")
plt.show()

# -----------------------------
# 3. CONFUSION MATRIX (MODEL A)
# -----------------------------

conf_matrix = pd.crosstab(df["model_A_prediction"], df["content_type"])

plt.figure()
sns.heatmap(conf_matrix, annot=True, fmt="d")
plt.title("Model A Confusion Matrix")
plt.show()
