from flask import Flask
# from data_table_V2 import db, EngineSensorData
from data_table_V1 import db, EngineTest1, EngineTest2, EngineTest3, EngineTest4, EngineTrain1, EngineTrain2, EngineTrain3, EngineTrain4
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
}


def load_dataset(dataset, path_file):
    with open(path_file, "r") as file:
        rows = []
        for ln, row in enumerate(file, start=1):
            row_data = parse_row(row)
            rows.append(dataset(**row_data))
    db.session.bulk_save_objects(rows)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        for dataset, (model, file_path) in data_sets.items():
            load_dataset(model, file_path)
