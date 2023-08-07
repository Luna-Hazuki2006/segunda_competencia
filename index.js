const { MongoClient } = require("mongodb")

const url = 'mongodb+srv://lunahazuki2006:cXU0lYhSncWZ12FM@cluster0.owjghpf.mongodb.net/'
const tabla = document.getElementById('tabla')
function mostrar() {
    MongoClient.connect(url, function(err, db) {
        if (err) throw err
        let transformacion = db.db('estudiantes')
        transformacion.collection('estudiantes').find(function(err, result) {
            if (err) throw err
            console.log(result);
            llenar(result)
            db.close()
        })
    })
}
function llenar(objeto) {
    let texto = ''
    for (const cosa in objeto) {
        texto += '<tr>'
        texto += '<td>' + cosa['nombre'] + '</td>'
        texto += '<td>' + cosa['edad'] + '</td>'
        texto += '<td>' + cosa['frase'] + '</td>'
        texto += '</tr>'
    }
    tabla.innerText += texto
}

mostrar()