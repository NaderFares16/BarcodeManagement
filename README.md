# Gerador de Código de Barras

Este repositório contém uma aplicação desenvolvida em Python, na qual permite gerar códigos de barras a partir de strings fornecidas através de requisições HTTP do tipo POST.

## Funcionalidades

- Geração de códigos de barras a partir de strings fornecidas pelo usuário.
- Resposta rápida e eficiente às requisições HTTP.
- Saída em formato de image contendo a string fornecida pelo usuário junto ao respectivo código de barras.

## Como usar

1. Clone o repositório a partir de GitHub;

```sh
  git clone https://github.com/NaderFares16/BarcodeManagement.git
```

2. Instale as dependências utilizadas no projeto:

```sh
  pip3 install -r requirements.txt
```

3. Inicie o servidor:

```sh
  py run.py
```

4. Adicione URL e inclua no Body da requisição POST um JSON contendo:

```sh
  http://localhost:3005/create_tag
```

```sh
  {
    "product_code": "{Codebar_Test}"
  }
```

Altere {Codebar_Test} por uma string de sua preferência, ao relizar a requisição, a aplicação retornará o código de barras!
