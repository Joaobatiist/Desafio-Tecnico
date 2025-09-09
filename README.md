# Desafio Técnico 

## Visão Geral do Projeto

Este projeto é uma API RESTful desenvolvida em **Python** com **Django** e **Django REST Framework (DRF)**. O objetivo é gerenciar Trilhas de Treinamento, permitindo a criação de trilhas que contêm etapas sequenciais. Cada etapa pode ter seus próprios recursos, como links e ligações, e o progresso pode ser rastreado.
 Documentação completa via Swagger.

## Funcionalidades Implementadas

A API oferece os seguintes endpoints para interação:

### Trilhas (`/api/trilhas/`)
- `POST /api/trilhas/`: Cria uma nova trilha de treinamento.
- `GET /api/trilhas/`: Lista todas as trilhas cadastradas.
- `GET /api/trilhas/{id}/`: Retorna os detalhes de uma trilha específica, incluindo suas etapas.
- `PUT /api/trilhas/{id}/`: Atualiza os dados de uma trilha.
- `DELETE /api/trilhas/{id}/`: Exclui uma trilha.

### Etapas (`/api/etapas/`)
- `POST /api/etapas/`: Cria uma nova etapa, vinculada a uma trilha existente.
- `GET /api/etapas/`: Lista todas as etapas cadastradas.
- `GET /api/etapas/{id}/`: Retorna os detalhes de uma etapa.
- `PUT /api/etapas/{id}/`: Atualiza os dados de uma etapa.
- `DELETE /api/etapas/{id}/`: Exclui uma etapa.

### Funcionalidade Adicional
- `POST /api/etapas/{id}/marcar_assistido/`: Marca uma etapa como concluída. Esta é uma ação personalizada que atualiza o status `assistido` para `true`.

## Como Executar o Projeto

Siga os passos abaixo para rodar a API em sua máquina local:

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    ```
2.  **Entre no diretório do projeto:**
    ```bash
    cd desafio-tecnico
    ```
3.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```
6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Documentação da API

A documentação interativa da API, que pode ser usada para testar todos os endpoints, está disponível no Swagger:

- **Swagger UI:** `http://127.0.0.1:8000/swagger/`

---
