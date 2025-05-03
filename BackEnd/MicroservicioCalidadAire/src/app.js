import express from 'express';
import config from './config.js';
import cors from 'cors';

import calidadAireRoutes from './routes/calidadAireRoutes.js';


const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('port', config.app.port);

app.use('/', calidadAireRoutes);

export default app;  