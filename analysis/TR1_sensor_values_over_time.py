import pandas as pd
from analysis.app.create_app import make_app
import matplotlib.pyplot as plt
from data_table import (db, EngineTrain1)


app = make_app()

with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)

engine_1 = df[df['unit_number'] == 1]
plt.figure(figsize=(15, 8))

for col in df.columns[5:]:
    plt.plot(engine_1['time_in_cycle'], engine_1[col], label=col)


plt.title('Raw Sensor Readings over Time (Engine 1)')
plt.xlabel('Cycle')
plt.ylabel('Sensor Value')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

