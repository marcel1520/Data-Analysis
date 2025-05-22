import pandas as pd
from analysis.app.create_app import make_app
import matplotlib.pyplot as plt
import numpy as np
from data_table import (db, EngineTrain1)


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
plt.show()

