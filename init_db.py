from flask import Flask
from data_table_V2 import db, EngineSensorData
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

with app.app_context():
    db.create_all()


def load_dataset(dataset_label, path_file):
    rows = []
    with open(path_file, "r") as file:
        for ln, row in enumerate(file, start=1):
            row_data = parse_row(row)
            row_data['dataset'] = dataset_label
            rows.append(EngineSensorData(**row_data))
    db.session.bulk_save_objects(rows)
    db.session.commit()


data_sets = [
    ("test_FD001.db", "CMAPSS-Data/test_FD001.txt"),
    ("test_FD002.db", "CMAPSS-Data/test_FD002.txt"),
    ("test_FD003.db", "CMAPSS-Data/test_FD003.txt"),
    ("test_FD004.db", "CMAPSS-Data/test_FD004.txt"),
    ("train_FD001.db", "CMAPSS-Data/train_FD001.txt"),
    ("train_FD002.db", "CMAPSS-Data/train_FD002.txt"),
    ("train_FD003.db", "CMAPSS-Data/train_FD003.txt"),
    ("train_FD004.db", "CMAPSS-Data/train_FD004.txt"),
]


if __name__ == "__main__":
    with app.app_context():
        for dataset_name, file_path in data_sets:
            load_dataset(dataset_name, file_path)
