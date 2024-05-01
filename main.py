from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2


class Item(BaseModel):
    name: str
    description: str
    price: float

class Rating(BaseModel):
    name: str
    description: str
    rating: float
    release_date: str


app = FastAPI()

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="test123",
                        port="5433")

cursor = conn.cursor() 


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/{urls}")
async def geturlitems(
    urls: str, num: int = 0, answer: int = 2):
    item = {"item_id": urls, "num": num, "answer": answer}
    return item



@app.get("/get_movies")
async def get_movies():
    cursor.execute("SELECT * FROM MOVIES")
    return cursor.fetchall()



@app.post("/add")
async def add_movie(rating: Rating):
    cursor.execute('''INSERT INTO MOVIES(NAME, DESCRIPTION, RATING, RELEASE_DATE
   ) VALUES ('{name}', '{description}', {rating}, '{release_date}')'''.format(name = rating.name,
                                            description = rating.description, 
                                            rating = rating.rating, 
                                            release_date = rating.release_date))

    conn.commit()


@app.post("/update_rating")
async def update_rating(name: str, new_rating: float):
    cursor.execute('''UPDATE MOVIES
    SET RATING = {new_rating}
    WHERE NAME = '{name}' '''.format(new_rating = new_rating, name = name))
    conn.commit()



@app.delete("/delete")
async def remove_movie(name: str):
    cursor.execute(f"DELETE FROM MOVIES WHERE NAME='{name}'")
    conn.commit()






conn.commit()

cursor.execute("SELECT * FROM MOVIES")
print(cursor.fetchall())
