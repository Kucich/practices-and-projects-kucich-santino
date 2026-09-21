import express from "express";
import fs from "fs";
import bodyParser from "body-parser";
import mysql from "mysql2"


// const mysql = require("mysql")
const conexion = mysql.createConnection(
    {
        host: "localhost",
        user: "root",
        password: "python1978",
        database: "greenjuegos"
    }
);

conexion.connect(function(err) {
    if(err) {
        throw err;
    } else{
        console.log("Conexion a bd exitosa.")
    };
});

// Operaciones CRUD de node a mysql

//Obtener datos de una tabla
function obtenerDatos() {
    conexion.query("SELECT * FROM productos", 
        function(error, filas) {
            if (error) {
                throw error;
            } else {
                filas.forEach(fila => {
                    console.log(fila)
                });
            }
        }
    );
};

obtenerDatos();

//Insertar un registro en una tabla
function insertarDatos() {
    conexion.query('INSERT INTO productos(nombre, cantidad) VALUES("Tobogan triple", 3);', (error, resultado) => {
        if (error) {
                throw error;
            } else {
                console.log("Producto registrado: ", resultado)
                };     
    });
};


//Modificicar datos de un registro
function modificarDatos() {
    conexion.query("UPDATE productos SET nombre = 'Calecita calabaza' WHERE nombre = 'Calecita';", (error, resultado) => {
        if (error) {
            throw error;
        } else {
            console.log("Producto modificado: ", resultado)
            };  
    });
};

//Eliminar registro de una tabla
function eliminarDatos() {
    conexion.query("DELETE FROM productos WHERE id = 10", (error, resultado) => {
        if (error) {
            throw error;
        } else {
            console.log("Producto eliminado: ", resultado)
            };  
    });
};

// eliminarDatos();
// obtenerDatos();

//---------------------------------------------//
// Creando endpoints de API con Express

const app = express()
app.use(bodyParser.json());

const readData = () => {
    try{
        const data = fs.readFileSync("./db.json");
        // console.log(JSON.parse(data))
        return JSON.parse(data);
    } catch(error) {
        console.log(error);
    }
};

const writeData = (data) => {
    try{
        fs.writeFileSync("./db.json", JSON.stringify(data));

    } catch(error) {
        console.log(error);
    }
};

// readData()

app.get("/usuarios", (req, res) => {
    const data = readData();
    res.send(data.usuarios);
});

app.get("/usuarios/:id", (req, res) => {
    const data = readData();
    const id = parseInt(req.params.id);
    const usuarios = data.usuarios.find((usuarios) => usuarios.id === id);
    res.json(usuarios);
});

app.post("/usuarios", (req, res) => {
    const data = readData();
    const body = req.body;
    const newUsuario = {
        id: data.usuarios.length + 1, ...body,
    };
    data.usuarios.push(newUsuario);
    writeData(data)
    res.json(newUsuario);
});

app.put("/productos/:id", (req, res) => {
    const data = readData();
    const body = req.body;
    const id = parseInt(req.params.id);
    const precioProducto = data.productos.find((productos) => productos.id === id);
    data.productos[precioProducto] = {
        ...data[precioProducto],
        ...body,
    };
    writeData(data);
    res.json({message: "Actualizacion completa."});
});

app.get("/", (req, res) => {
    res.send("Mi primera api super!!!!");
});

app.listen(3000, () => {
    console.log("Servidor escuchando en 3000"); 
});
