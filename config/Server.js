// yarn add express
// forma de importar usando js puro
const express = require("express")

class Server{
  constructor(){
    this.app = express()
    //process.env => mira las variables de entorno en la maquina
    this.puerto = process.env.PORT || 8000;
  }
  iniciarServidor(){
    this.app.listen(this.puerto,() => {
      console.log(`Servidor corriendo exitosamente: 127.0.0.1:${this.puerto}`);
    });
  }
}

module.exports = {
  Server,
};