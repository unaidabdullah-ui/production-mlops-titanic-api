from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd

def detect_drift():
    ref = pd.read_csv("data/raw/titanic.csv")
    curr = ref.sample(frac=1.0)

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=curr)

    report.save_html("drift_report.html")

if __name__ == "__main__":
    detect_drift()