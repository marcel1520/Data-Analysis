from analysis.app.create_app import make_app
import pandas as pd
from data_table import (db, EngineTrain1)
import matplotlib.pyplot as plt
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

app = make_app()

with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)


selected_engines = [1, 10, 20]
sensor_to_plot = "sensor_2"

plt.figure(figsize=(15, 6))

for unit in selected_engines:
    engine_df = df[df["unit_number"] == unit]
    plt.plot(engine_df["time_in_cycle"], engine_df[sensor_to_plot], label=f"Engine{unit}")

plt.xlabel("Cycle")
plt.ylabel(sensor_to_plot)
plt.title(f"{sensor_to_plot} Over time for selected Engines")
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


