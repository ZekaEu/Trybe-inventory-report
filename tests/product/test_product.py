from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        99,
        "Magic: The Gathering",
        "Wizards of The Coast - @Hasbro",
        1993,
        2019,
        "M20-212/280",
        "Sleeve/Shield"
    )

    assert produto.id == 99
    assert produto.nome_do_produto == "Magic: The Gathering"
    assert produto.nome_da_empresa == "Wizards of The Coast - @Hasbro"
    assert produto.data_de_fabricacao == "1993"
    assert produto.data_de_validade == "2019"
    assert produto.numero_de_serie == "M20-212/280"
    assert produto.instrucoes_de_armazenamento == "Sleeve/Shield"
