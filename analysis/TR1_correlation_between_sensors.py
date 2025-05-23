import pandas as pd
import seaborn as sns
from analysis.app.create_app import make_app
import matplotlib.pyplot as plt
from data_table import (db, EngineTrain1)
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv(".env")
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

app = make_app()

with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)

sensor_cols = []
for col in df.columns:
    if col.startswith('sensor_'):
        sensor_cols.append(col)
sensor_df = df[sensor_cols]

correlation_matrix = sensor_df.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Sensor correlation heatmap")
plt.savefig('sensor_plot.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

user_prompt = input("Enter your prompt: ")
model = genai.GenerativeModel('gemini-1.5-flash')
with open('sensor_plot.png', "rb") as img_file:
    image_data = img_file.read()

response = model.generate_content([
    {'mime_type': 'image/png', 'data': image_data},
    user_prompt
])

print(response.text)
