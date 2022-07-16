from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product_list):
        company_and_quantity = ""
        simpĺe_report = SimpleReport.generate(product_list)
        company_list = [product["nome_da_empresa"] for product in product_list]
        company_dict = dict(Counter(company_list))

        for company, quantity in company_dict.items():
            company_and_quantity += f"- {company}: {quantity}\n"

        return (
          f"{simpĺe_report}\n"
          "Produtos estocados por empresa:\n"
          f"{company_and_quantity}"
        )
