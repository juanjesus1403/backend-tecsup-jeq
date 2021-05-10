import {Router} from 'express'
import {crearTarea, listarTareas, listarTareasPorId} from "../controllers/tareas"

export const tareas_router = Router();

tareas_router.route("/tareas").post(crearTarea).get(listarTareas);
// para ahcer un parametro x url DINAMICO simplemente definimos el nombre de esa variable pero con ":" para que express sepa que sera dinamico 
//
tareas_router.route("/tareas/:id").get(listarTareasPorId)
