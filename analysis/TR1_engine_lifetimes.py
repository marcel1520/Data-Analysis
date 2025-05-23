import pandas as pd
from analysis.app.create_app import make_app
import matplotlib.pyplot as plt
import numpy as np
from data_table import (db, EngineTrain1)
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

app = make_app()

with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)


cycle_counts = df.groupby('unit_number')['time_in_cycle'].max()
cycle_counts.hist(bins=30, figsize=(8, 4))
plt.title('Distribution of Engine Lifespan (Cycles)')
plt.xlabel('Max Cycles')
plt.ylabel('Number of Engines')
plt.grid(True)

min_cycles = cycle_counts.min()
max_cycles = cycle_counts.max()
plt.xticks(np.arange(min_cycles - (min_cycles % 25), max_cycles + 25, 25))
plt.xticks(rotation=45)
plt.tight_layout()
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