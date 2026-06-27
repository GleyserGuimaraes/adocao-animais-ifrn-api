from fastapi import FastAPI

app = FastAPI(
    title="API Adoção de Animais",
    version="1.0.0",
    description="API REST para gerenciamento de animais disponíveis para adoção."
)

@app.get("/")
def inicio():
    return {
        "mensagem": "API de Adoção de Animais em execução."
    }

