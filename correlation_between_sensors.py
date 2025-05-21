from flask import Flask
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_table_V1 import (db, EngineTest1, EngineTest2, EngineTest3, EngineTest4,
                           EngineTrain1, EngineTrain2, EngineTrain3, EngineTrain4,
                           RUL1, RUL2, RUL3, RUL4)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engine_data_complete.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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
