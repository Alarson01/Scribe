from datetime import datetime
import os


def save_report(report):

    os.makedirs("outputs", exist_ok=True)

    filename = datetime.now().strftime(
        "outputs/report_%Y%m%d_%H%M.md"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    print("Rapport enregistré :", filename)
