from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_table_columns(table_name, class_name):
    columns = {
        "__tablename__": table_name,
        "id": db.Column(db.Integer, primary_key=True, autoincrement=True),
        "unit_number": db.Column(db.Integer),
        "time_in_cycle": db.Column(db.Integer),
        "op_setting_1": db.Column(db.Float),
        "op_setting_2": db.Column(db.Float),
        "op_setting_3": db.Column(db.Float),
    }

    for i in range(1, 22):
        columns[f"sensor_{i}"] = db.Column(db.Float)

    return type(class_name, (db.Model,), columns)

EngineTest1 = create_table_columns("test_FD001", "EngineTestFD001")
EngineTest2 = create_table_columns("test_FD002", "EngineTestFD002")
EngineTest3 = create_table_columns("test_FD003", "EngineTestFD003")
EngineTest4 = create_table_columns("test_FD004", "EngineTestFD004")

EngineTrain1 = create_table_columns("train_FD001", "EngineTrainFD001")
EngineTrain2 = create_table_columns("train_FD002", "EngineTrainFD002")
EngineTrain3 = create_table_columns("train_FD003", "EngineTrainFD003")
EngineTrain4 = create_table_columns("train_FD004", "EngineTrainFD004")
