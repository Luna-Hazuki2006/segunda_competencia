console.log('holaaaaaaaaaaaaaaaaaaaaaaaaaaa');
// import { MongoClient } from "mongodb";
const { MongoClient } = require("mongodb")
require('dotenv').config()
const mongoClient = new MongoClient(process.env.MONGODB_URI)
const clientePromesa = mongoClient.connect()
const manejador = async (event) => {
    try {
        const database = (await clientePromesa).db(process.env.MONGODB_DATABASE)
        const collection = database.collection(process.env.MONGODB_COLLECTION)
        const resultados = await collection.find({}).limit(10).toArray()
        console.log(resultados);
        mongoClient.close(true)
        return {
            statusCode: 200, 
            body: JSON.stringify(resultados)
        }
    } catch (error) {
        return { statusCode: 500, body: error.toString() }
    }
}
manejador()
const esto = document.createElement('p')
esto.innerText = "lo logré"
esto.style.color = "red"
document.getElementById('cuerpo').appendChild(esto)