from flask import Blueprint, render_template, request
import pandas as pd
from data_table import db, EngineTrain1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["GET", "POST"])
def dashboard():
    df = pd.read_sql(EngineTrain1.__table__.select(), db.engine)
    unit_numbers = sorted(df["unit_number"].unique().tolist())
    selected_unit = request.form.get("unit_number", unit_numbers[0])
    selected_setting = request.form.get("setting", "op_setting_1")

    plot_url = None
    if request.method == "POST":
        filtered = df[df["unit_number"] == int(selected_unit)]

        fig, ax = plt.subplots(figsize=(15, 7))

        ax.plot(filtered["time_in_cycle"], filtered[selected_setting])

        ax.set_title(f"For Engine {selected_unit} - {selected_setting}")
        ax.set_xlabel("Cycle")
        ax.set_ylabel("Settings Graph")
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        ax.grid(True)

        buf = io.BytesIO()
        plt.tight_layout()
        fig.savefig(buf, format="png")
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode("utf-8")
        plt.close()

    return render_template("dashboard.html",
                           unit_numbers=unit_numbers,
                           selected_unit=int(selected_unit),
                           selected_setting=selected_setting,
                           plot_url=plot_url)

