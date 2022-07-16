import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if "csv" in path:
            with open(path, "r") as file:
                products_csv = csv.DictReader(file)
                product_list = [product for product in products_csv]

            if report_type == "simples":
                return SimpleReport.generate(product_list)

            return CompleteReport.generate(product_list)
