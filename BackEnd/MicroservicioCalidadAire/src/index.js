import app from './app.js';  
import dotenv from 'dotenv';

dotenv.config();

app.listen(app.get('port'), () => {
    console.log(`Server running on port ${app.get('port')}`);
});