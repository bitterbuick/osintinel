# src/report_generator.py

import json
import os

class ReportGenerator:
    @staticmethod
    def save_report(data, filename):
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reports")
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        filepath = os.path.join(reports_dir, filename)
        with open(filepath, 'w') as report_file:
            json.dump(data, report_file, indent=4)
        print(f"Report saved to {filepath}")

# Example usage
if __name__ == "__main__":
    sample_data = {"example": "data"}
    ReportGenerator.save_report(sample_data, "sample_report.json")

