import express from 'express';
import config from './config.js';
import cors from 'cors';

import { fileURLToPath } from 'url';


import reconocimientoRoutes from './routes/reconocimientoRoutes.js';


import calidadAireRoutes from './routes/calidadAireRoutes.js';


const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/modelos', express.static(path.join(__dirname, '../../..', 'modelos')));

app.set('port', config.app.port);

app.use('/', calidadAireRoutes);

export default app;  