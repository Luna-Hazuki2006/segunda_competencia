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
    } catch (error) {
        return { statusCode: 500, body: error.toString() }
    }
}
manejador()
// module.exports = { manejador }

// const tabla = document.getElementById('tabla')
// function mostrar() {
//     MongoClient.connect(url, function(err, db) {
//         if (err) throw err
//         let transformacion = db.db('estudiantes')
//         transformacion.collection('estudiantes').find(function(err, result) {
//             if (err) throw err
//             console.log(result);
//             // llenar(result)
//             db.close()
//         })
//     })
// }
// function llenar(objeto) {
//     let texto = ''
//     for (const cosa in objeto) {
//         texto += '<tr>'
//         texto += '<td>' + cosa['nombre'] + '</td>'
//         texto += '<td>' + cosa['edad'] + '</td>'
//         texto += '<td>' + cosa['frase'] + '</td>'
//         texto += '</tr>'
//     }
//     tabla.innerText += texto
// }

// mostrar()