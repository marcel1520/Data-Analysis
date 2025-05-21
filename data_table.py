from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_table_test_train(table_name, class_name):
    columns = {
        "__tablename__": table_name,
        "id": db.Column(db.Integer, primary_key=True, autoincrement=True),
        "unit_number": db.Column(db.Integer, nullable=False),
        "time_in_cycle": db.Column(db.Integer, nullable=False),
        "op_setting_1": db.Column(db.Float, nullable=False),
        "op_setting_2": db.Column(db.Float, nullable=False),
        "op_setting_3": db.Column(db.Float, nullable=False),
    }

    for i in range(1, 22):
        columns[f"sensor_{i}"] = db.Column(db.Float, nullable=False)

    return type(class_name, (db.Model,), columns)


def create_table_rul(table_name, class_name):
    columns = {
        "__tablename__": table_name,
        "id": db.Column(db.Integer, primary_key=True, autoincrement=True),
        "unit_number": db.Column(db.Integer, unique=True, nullable=False),
        "rul": db.Column(db.Integer, nullable=False)
    }
    return type(class_name, (db.Model,), columns)

EngineTest1 = create_table_test_train("test_FD001", "EngineTestFD001")
EngineTest2 = create_table_test_train("test_FD002", "EngineTestFD002")
EngineTest3 = create_table_test_train("test_FD003", "EngineTestFD003")
EngineTest4 = create_table_test_train("test_FD004", "EngineTestFD004")

EngineTrain1 = create_table_test_train("train_FD001", "EngineTrainFD001")
EngineTrain2 = create_table_test_train("train_FD002", "EngineTrainFD002")
EngineTrain3 = create_table_test_train("train_FD003", "EngineTrainFD003")
EngineTrain4 = create_table_test_train("train_FD004", "EngineTrainFD004")

RUL1 = create_table_rul("rul_FD001", "RUL_FD001")
RUL2 = create_table_rul("rul_FD002", "RUL_FD002")
RUL3 = create_table_rul("rul_FD003", "RUL_FD003")
RUL4 = create_table_rul("rul_FD004", "RUL_FD004")
