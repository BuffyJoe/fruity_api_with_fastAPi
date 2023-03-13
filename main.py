from fastapi import FastAPI
from models import Fruits, updateFruits
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
fruitsSeen : list[Fruits] = [
    Fruits(
      name= 'Pineapple',
    day_first_seen= '12th October, 2020',

    condition='ripe',
    # location= 'Amawbia'
    ),
    Fruits(
      name='Apple',
    day_first_seen= '12th January, 2020',
    condition= 'overripe',
    # location='Okpunno'
    ),
    Fruits(
      name='Strawberry',
    day_first_seen= '12th November, 2020',
    condition='ripe',
    # location='ifite'
    ),
    Fruits(
      name= 'Mango',
    day_first_seen='12th August, 2020',
    condition='unripe',
    # location='Ngozika'
    ),
    Fruits(
    name= 'Udala',
    day_first_seen='12th June, 2020',
    condition='ripe',
    # location='Ifite'
    ),
]


@app.get("/")
async def fruitList():
    return fruitsSeen



@app.get("/{search_name}?")
async def singleFruit(search_name):
    for fruit in fruitsSeen:
        if fruit.name == search_name:
            fruits = fruit
            return fruits
        
@app.post('/add_fruit/')
async def addFruit(fruit: Fruits):
    fruitsSeen.append(fruit)
    return fruit

@app.put('/edit/{fruit_name}')
async def editFruit(fruit: updateFruits, fruit_name: str):
    print(fruit_name)
    for i in fruitsSeen:
        if i.name == fruit_name:
            if fruit.condition is not None:
                i.condition = fruit.condition
                
            if fruit.day_last_seen is not None:
                i.day_last_seen = fruit.day_last_seen
            if fruit.price is not None:
                i.price = fruit.price
            if fruit.image is not None:
                i.image = fruit.image
            return
        
@app.delete("/delete/{fruit_name}")
async def deleteFruit(fruit_name):
    for fruit in fruitsSeen:
        if fruit.name == fruit_name:
            fruitsSeen.remove(fruit)
            return