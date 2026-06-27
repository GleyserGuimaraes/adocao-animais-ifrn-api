# API ADOCAO DE ANIMAIS

API REST desenvolvida com FastAPI para gerenciamento de animais disponíveis para adoção e registro de adoções. Este projeto foi desenvolvido com fins acadêmicos para demonstrar conceitos de Engenharia de Software, desenvolvimento de APIs REST, modelagem de dados e boas práticas de organização de projetos utilizando FastAPI.

O principal objetivo é simular a entrada de um novo desenvolvedor em uma equipe de software que já possui um sistema em desenvolvimento. Este projeto representa uma aplicação em desenvolvimento mantida por uma equipe de software. Assim como ocorre em projetos reais, o código apresenta funcionalidades parcialmente implementadas, pequenas inconsistências, trechos que podem ser refatorados e oportunidades de melhoria. Durante a atividade, o participante deverá compreender a arquitetura existente, identificar problemas e evoluir a aplicação conforme os requisitos propostos.

Durante a execução do projeto, são trabalhados conceitos como:

- Leitura e compreensão de código existente;
- Estruturação de APIs REST utilizando FastAPI;
- Modelagem e validação de dados com Pydantic;
- Organização de projetos em camadas;
- Controle de versões com Git;
- Desenvolvimento incremental de funcionalidades;
- Documentação de software;
- Correção de pequenos defeitos e evolução de software;
- Boas práticas de desenvolvimento e manutenção de sistemas.

---

## Funcionalidades

### Animais

- Cadastrar animais para adoção
- Listar animais cadastrados
- Consultar um animal por ID
- Atualizar informações de um animal
- Remover animal

### Adoções

- Registrar adoção de um animal
- Listar adoções realizadas
- Impedir adoção de animais já adotados
- Atualizar automaticamente o status do animal após adoção

---

## Regras de Negócio

- Um animal só pode ser adotado uma única vez.
- Apenas animais disponíveis podem ser adotados.
- Após a adoção, o status do animal é alterado para **Adotado**.
- Não é permitido registrar adoção para animais inexistentes.
- Para mais detalhes verificar o arquivo de requisitos

---

## Tecnologias Utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

---


## Executando a Aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```text
http://localhost:8000
```

---

## 📚 Documentação da API

O FastAPI gera automaticamente a documentação interativa.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## Endpoints 

### Animais

| Método | Endpoint | Descrição |
|----------|------------|------------|
| GET | /animais | Lista todos os animais |
| GET | /animais/{id} | Consulta um animal |
| POST | /animais | Cadastra um animal |
| PUT | /animais/{id} | Atualiza um animal |
| DELETE | /animais/{id} | Remove um animal |

### Adoções

| Método | Endpoint | Descrição |
|----------|------------|------------|
| GET | /adocoes | Lista todas as adoções |
| POST | /adocoes | Registra uma adoção |

---

## Exemplo de Cadastro de Animal

### Requisição

```json
{
  "nome": "Rex",
  "especie": "Cachorro",
  "raca": "Caramelo",
  "idade": 3,
  "porte": "Médio"
}
```

### Resposta

```json
{
  "id": 1,
  "nome": "Rex",
  "especie": "Cachorro",
  "raca": "Caramelo",
  "idade": 3,
  "porte": "Médio",
  "status": "Disponível"
}
```

---

## Exemplo de Registro de Adoção

### Requisição

```json
{
  "nome_adotante": "Maria Silva",
  "telefone": "(83) 99999-9999",
  "email": "maria@email.com",
  "id_animal": 1
}
```

### Resposta

```json
{
  "mensagem": "Adoção registrada com sucesso."
}
```

---


## Autor

**Gleyser Guimarães**

Professor de Informática | Desenvolvedor de Software
