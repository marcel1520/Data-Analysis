from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_table_V1 import (db, EngineTest1, EngineTest2, EngineTest3, EngineTest4,
                           EngineTrain1, EngineTrain2, EngineTrain3, EngineTrain4,
                           RUL1, RUL2, RUL3, RUL4)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///engine_data_complete.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)

plt.figure(figsize=(14, 6))
sns.violinplot(x='unit_number', y='sensor_2', data=df[df['unit_number'] <= 10])
plt.title('Sensor 2 Distributuion (Violin Plot) - First 10 Engines')
plt.xlabel('Engine Unit Number')
plt.ylabel('Sensor')
plt.show()

