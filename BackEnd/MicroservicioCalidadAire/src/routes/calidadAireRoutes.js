import { Router } from 'express';
import { obtenerCalidadDeAire } from '../controllers/calidadAireController.js';

const router = Router();

router.get('/calidad-aire', obtenerCalidadDeAire);

export default router;
