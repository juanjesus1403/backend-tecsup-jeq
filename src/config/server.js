import express from "express";
import {json} from "body-parser";
import {conexion} from "./sequelize"

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
    this.app.listen(this.port, async () => {
      console.log(`Servidor corriendo en: http://127.0.0.1:${this.port}`);
      try{
        //esto va a tratar de conectarse con el servidor usando las credenciales definidas anteriormente
        //alter => si hubo algun cambio en la bd volvera a generar SOLAMENTE esos cambios
        //force => RESETEA (borra) toda la bd y su contenido y lo vuelve a crear de 0, NUNCA USAR ESTO EN MODO PRODUCCION
        await conexion.sync();
        console.log("Base de datos sincronizada correctamente");
      } catch (error){
        console.error(error);
  
      }
    });
  }
}