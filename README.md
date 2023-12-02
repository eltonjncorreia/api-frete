# Api Frete

API Rest para calcular frete.

Essa API fornece preço de frete em diferentes transportadoras.

![architecture](/arch.png)


# Como funciona ?



# Como executar ?



# Como está organizado ?

A arquitetura segue a seguinte estrutura:

    infra
        |___api

    shipping_service
        |__domain
            |____ product
            |____ shipping

        |__usecases
            |____ services

    tests
        |___ shipping_service


# Testes

Para executar os testes, entre na raiz do projeto e execute o comando.

`pytest -vvv tests/`