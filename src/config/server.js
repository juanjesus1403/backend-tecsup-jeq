import express from "express";
import {json} from "body-parser";

export default class Server {
  constructor(){
    this.app = express(),
    this.port = process.env.PORT || 8000;
    this.bodyParser();
  }
  bodyParser(){
    //sirve para configurar la forma en la cual el API REST va a recibir datos del front mediante el body
    this.app.use(json());
  }
  start(){
    // sirve para levantar el servidor en el cual le tenemos que pasar el puerto y si todo es exitoso ingresaremos al callback(segundo parametro)
    this.app.listen(this.port,()=>{
      console.log(`Servidor corriendo en: http://127.0.0.1:${this.port}`)
    })
  }
}