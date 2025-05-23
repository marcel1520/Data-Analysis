from analysis.app.create_app import make_app
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_table import (db, EngineTrain1)


app = make_app()

with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)

plt.figure(figsize=(14, 6))
sns.violinplot(x='unit_number', y='sensor_2', data=df[df['unit_number'] <= 10])
plt.title('Sensor 2 Distribution (Violin Plot) - First 10 Engines')
plt.xlabel('Engine Unit Number')
plt.ylabel('Sensor')
plt.show()

