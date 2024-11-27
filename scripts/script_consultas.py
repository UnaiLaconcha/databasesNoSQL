import pymongo

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bd_nosql"]

# Consultar las jugadoras mayores de 25 años
collection = db["jugadoras"]
resultado = collection.find({"edad": {"$gt": 25}})

print("Jugadoras mayores de 25 años:")
for jugadora in resultado:
    print(jugadora)
