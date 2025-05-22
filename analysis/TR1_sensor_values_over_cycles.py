from analysis.app.create_app import make_app
import pandas as pd
from data_table import (db, EngineTrain1)


app = make_app()


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

