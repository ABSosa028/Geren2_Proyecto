import express from 'express';
import config from './config.js';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();

/*carga estatica de modelo y otros archivos publicos */
app.use(express.static(path.join(__dirname, 'src/public')));

/*configuracion de renderizado de views */
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.set('port', config.app.port);

app.use(express.static(path.join(__dirname, 'public')));

/*configuracion basica de express y peticiones de views */
app.use(cors());
app.use(express.json({ limit: '20mb' }));/*20mb pa que aguante archivos grandes, si no no jala */
app.use(express.urlencoded({ extended: true, limit: '20mb' }));

/*urls asignadas para vistas */
app.get('/analizar-numeros', (req, res) => {
    res.render('analizar-numeros');
});

app.get('/analizar-gestos', (req, res) => {
    res.render('analizar-gestos');
});

app.use('/modelos', express.static(path.join(__dirname, '../../..', 'modelos')));

app.get('/', (req, res) => {
    res.render('index', { titulo: 'Bienvenido a mi proyecto'});
});

app.get('/dashboard', (req, res) => {
    res.render('dashboard');
});


app.get('/login', (req, res) => {
    res.render('login');
});

/*urls asignadas para funcionamiento*/
app.post('/login', (req, res) => {
    const { usuario, contrasena } = req.body;
    console.log('Usuario:', usuario);
    console.log('Contraseña:', contrasena);
    if (usuario === 'admin' && contrasena === 'admin') {
        res.redirect('/dashboard');
    }
});

app.post('/api/comprobar-numero', (req, res) => {
    const { imagen } = req.body;
    console.log('Imagen recibida (base64):', imagen.substring(0, 100)); 

    res.json({ resultado: 7 });
});

app.post('/api/comprobar-gesto', (req, res) => {
    const { imagen } = req.body;
    console.log('Imagen recibida (gesto base64):', imagen.substring(0, 100));
    res.json({ resultado: '👍 (ejemplo)' });
});


export default app;
