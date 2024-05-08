from fastapi import FastAPI
from pandas import pandas as pd

app = FastAPI()

result_df = pd.read_csv("C:/Users/Federico/Desktop/Trabajo Individual Henry/1/FastApi/CSV/UserForGenre.csv")
df_max_hours_year = pd.read_csv("C:/Users/Federico/Desktop/Trabajo Individual Henry/1/FastApi/CSV/PlayTimeGenres.csv")

@app.get("/user_for_genre/{genre}")
def UserForGenre(genre: str):
    # Suponiendo que tienes el DataFrame 'df' disponible en este contexto
    genre_df = result_df[result_df["genres"] == genre]
    
    # Encontrar el índice del usuario que más jugó para ese género
    max_playtime_index = genre_df["playtime_forever"].idxmax()
    
    # Obtener el usuario y las horas correspondientes
    max_playtime_user = genre_df.loc[max_playtime_index, "user_id"]
    max_playtime_hours = genre_df.loc[max_playtime_index, "playtime_forever"]
    
    return max_playtime_user, max_playtime_hours

@app.get("/play_time_genre/{genre}")
def PlayTimeGenre(genre: str):
    # Filtrar el DataFrame por el género especificado
    df_genre = df_max_hours_year[df_max_hours_year['genre'] == genre]
    
    # Verificar si se encontraron datos para el género especificado
    if df_genre.empty:
        return None
    
    # Obtener el año correspondiente al género con mayor tiempo jugado
    año_max_playtime = df_genre.loc[df_genre['playtime_forever'].idxmax(), 'year']
    
    return año_max_playtime