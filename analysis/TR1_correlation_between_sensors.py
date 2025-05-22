import pandas as pd
import seaborn as sns
from analysis.app.create_app import make_app
import matplotlib.pyplot as plt
from data_table import (db, EngineTrain1)


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
plt.show()
