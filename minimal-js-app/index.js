const express = require('express');
const pino = require('pino-http')({
	useLevel: process.env.LOG_LEVEL || 'info'
});

const app = express();
const port = process.env.PORT || 8080;

app.use(pino);

app.get('/', (req, res) => {
	req.log.info();
	const target = process.env.TARGET || 'World';
	res.send(`Hello ${target}!\n`);
});

app.get('/errorz', (req, res) => {
	req.log.error();
	res.status(500).send('Something broke!');
});

app.get('/healthz', (req, res) => {
	req.log.info();
	res.send('{"status":"ok"}');
});

app.listen(port, () => {
	console.log('Demo application listening on port', port);
});
