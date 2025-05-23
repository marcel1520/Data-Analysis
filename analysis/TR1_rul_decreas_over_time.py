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

df['max_cycle'] = df.groupby('unit_number')['time_in_cycle'].transform('max')
df['RUL'] = df['max_cycle'] - df['time_in_cycle']

sample_engines = [1, 10, 20]
plt.figure(figsize=(10, 5))

for unit in sample_engines:
    temp = df[df['unit_number'] == unit]
    plt.plot(temp['time_in_cycle'], temp['RUL'], label=f'Engine {unit}')


plt.xlabel('Cycle')
plt.ylabel('Remaining Useful Life (RUL)')
plt.title('RUL Curves for Selected Engines')
plt.legend()
plt.grid(True)
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

