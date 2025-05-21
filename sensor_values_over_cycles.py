from flask import Flask
import pandas as pd
from data_table_V1 import (db, EngineTest1, EngineTest2, EngineTest3, EngineTest4,
                           EngineTrain1, EngineTrain2, EngineTrain3, EngineTrain4,
                           RUL1, RUL2, RUL3, RUL4)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engine_data_complete.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)

import matplotlib.pyplot as plt

selected_engines = [1, 10, 20]
sensor_to_plot = "sensor_2"

plt.figure(figsize=(10, 6))

for unit in selected_engines:
    engine_df = df[df["unit_number"] == unit]
    plt.plot(engine_df["time_in_cycle"], engine_df[sensor_to_plot], label=f"Engine{unit}")

plt.xlabel("Cycle")
plt.ylabel(sensor_to_plot)
plt.title(f"{sensor_to_plot} Over time for selected Engines")
plt.legend()
plt.grid(True)
plt.show()

