from flask import Flask
# from data_table_V2 import db, EngineSensorData
from data_table_V1 import (db, EngineTest1, EngineTest2, EngineTest3, EngineTest4,
                           EngineTrain1, EngineTrain2, EngineTrain3, EngineTrain4,
                           RUL1, RUL2, RUL3, RUL4)
from headers_listed import headers_listed


headers = headers_listed


def float_or_int(val):
    if "." in val:
        return float(val)
    return int(val)


def parse_row(row):
    values = row.strip().split()
    parsed = dict(zip(headers, map(float_or_int, values)))
    return parsed


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///engine_data_complete.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


data_sets = {
    "test_FD001": (EngineTest1, "CMAPSS-Data/test_FD001.txt"),
    "test_FD002": (EngineTest2, "CMAPSS-Data/test_FD002.txt"),
    "test_FD003": (EngineTest3, "CMAPSS-Data/test_FD003.txt"),
    "test_FD004": (EngineTest4, "CMAPSS-Data/test_FD004.txt"),
    "train_FD001": (EngineTrain1, "CMAPSS-Data/train_FD001.txt"),
    "train_FD002": (EngineTrain2, "CMAPSS-Data/train_FD002.txt"),
    "train_FD003": (EngineTrain3, "CMAPSS-Data/train_FD003.txt"),
    "train_FD004": (EngineTrain4, "CMAPSS-Data/train_FD004.txt"),
    "rul_FD001": (RUL1, "CMAPSS-Data/RUL_FD001.txt"),
    "rul_FD002": (RUL2, "CMAPSS-Data/RUL_FD002.txt"),
    "rul_FD003": (RUL3, "CMAPSS-Data/RUL_FD003.txt"),
    "rul_FD004": (RUL4, "CMAPSS-Data/RUL_FD004.txt"),
}


def load_dataset(dataset, path_file):
    rows = []
    is_rul = dataset.__tablename__.startswith("rul_")
    with open(path_file, "r") as file:
        for idx, row in enumerate(file, start=1):
            if is_rul:
                rul_val = float_or_int(row.strip())
                rows.append(dataset(unit_number=idx, rul=rul_val))
            else:
                row_data = parse_row(row)
                rows.append(dataset(**row_data))

    db.session.bulk_save_objects(rows)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        for dataset, (model, file_path) in data_sets.items():
            load_dataset(model, file_path)
