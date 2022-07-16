import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, "r") as file:
            if "csv" in path:
                products_csv = csv.DictReader(file)
                product_list = [product for product in products_csv]
            elif "json" in path:
                product_list = json.load(file)

            if report_type == "simples":
                return SimpleReport.generate(product_list)

            return CompleteReport.generate(product_list)
