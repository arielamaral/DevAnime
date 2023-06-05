from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de animes"}

@app.get("/animes/{anime_id}")
def get_anime(anime_id: int):
    return {"anime_id": anime_id, "title": "Exemplo de Anime"}

@app.post("/animes")
def create_anime(anime: dict):
    # Aqui você pode tratar a criação de um novo anime no banco de dados
    return {"message": "Anime criado com sucesso", "anime": anime}
