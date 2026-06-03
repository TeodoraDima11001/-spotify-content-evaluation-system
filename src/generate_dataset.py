import pandas as pd
import numpy as np

np.random.seed(42)

n = 500  # number of rows

content_types = ["music", "podcast", "audiobook", "mixed"]
languages = ["EN", "RO", "ES", "FR"]

data = {
    "content_id": range(1, n + 1),
    
    "title": ["Content_" + str(i) for i in range(n)],
    
    "description": np.random.choice([
        "music track with vocals",
        "spoken podcast episode",
        "audiobook narration",
        "mixed media content with speech and music"
    ], n),
    
    "content_type": np.random.choice(content_types, n),
    
    "duration_sec": np.random.randint(30, 3600, n),
    
    "language": np.random.choice(languages, n),
    
    "explicit_flag": np.random.choice([0, 1], n),
    
    # human labels (simulate real annotation noise)
    "human_label": np.random.choice(content_types, n),
    
    # model predictions
    "model_A_prediction": np.random.choice(content_types, n),
    "model_B_prediction": np.random.choice(content_types, n),
    
    # confidence scores
    "model_A_confidence": np.random.rand(n),
    "model_B_confidence": np.random.rand(n),
    
    # engagement signals
    "views": np.random.randint(100, 10000, n),
    "likes": np.random.randint(0, 5000, n),
    "skips": np.random.randint(0, 3000, n),
    "completion_rate": np.random.rand(n)
}

df = pd.DataFrame(data)

df.to_csv("content_dataset.csv", index=False)

print("Dataset created successfully!")
print(df.head())
