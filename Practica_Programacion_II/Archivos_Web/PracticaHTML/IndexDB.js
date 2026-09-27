const salidaEL = document.getElementById("salida")

const salida = (msg) => {
    if (salidaEL) {
        salidaEL.textContent = JSON.stringify(msg, null, 2);
    }
};

const db = await new Promise((resolve, reject) => {
    const req = indexedDB.open("demo", 1); // Crea una BD

    // Crea o accede a la tabla productos
    req.onupgradeneeded = () => req.result.createObjectStore("productos", {keyPath: "id", autoIncrement:true});

    // Devuelve el resultado 
    req.onsuccess = () => resolve(req.result);

    // En caso de error te dice cual es
    req.onerror = () => reject(req.error);
    }
);



const store = (mode) => {
    return db.transaction("productos", mode).objectStore("productos");
}


const put = (producto) => 
    new Promise((res, rej) => {
    const req = store("readwrite").put(producto);
    req.onsuccess = () => res(req.result);
    req.onerror = () => rej(req.error);
});


// Obtener todo de una base de datos del navegador, ejemplo: sobre un usuario 
const getall = () => new Promise((res, rej) => {
    const req = store("readonly").getAll();
    req.onsuccess = () =>res(req.result);
    req.onerror = () => rej(req.error);
});


agregar.onclick = async () => await put({
    nombre: nombre.value,
    precio: +precio.value
});

obtener.onclick = async () => salida(await getall());


const eliminar = (id) =>
    new Promise((res, rej) => {
        const req = store("readwrite").delete(id);

        req.onsuccess = () => res();
        req.onerror = () => rej(req.error);
    });
