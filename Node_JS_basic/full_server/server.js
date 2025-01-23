// Small Server that get the routes from routes

import router from './routes';

const express = require('express');

const port = 1245;
const app = express();

app.use('/', router);

app.listen(port);

export default app;