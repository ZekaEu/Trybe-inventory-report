class SimpleReport:
    oldest_product = ""
    nearest_to_expire = ""
    biggest_company = ""

    @classmethod
    def generate(cls, product_list):
        cls.oldest_product = min(
            [product["data_de_fabricacao"] for product in product_list]
        )

        cls.nearest_to_expire = min(
            [product["data_de_validade"] for product in product_list]
        )

        company_list = [product["nome_da_empresa"] for product in product_list]
        cls.biggest_company = max(company_list, key=company_list.count)

        return (
           f"Data de fabricação mais antiga: {cls.oldest_product}\n"
           f"Data de validade mais próxima: {cls.nearest_to_expire}\n"
           f"Empresa com mais produtos: {cls.biggest_company}"
        )
