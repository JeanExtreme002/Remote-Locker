const router = require("./controller/routes");
const express = require("express");
const bodyParser = require("body-parser");
const app = express();

// Configurações.
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(router);

// Obtém o Port Number do servidor.
const PORT = process.env.PORT || 5000;

// Inicializa o servidor.
app.listen(PORT, function() {
    console.log(`Running server on port ${PORT}`);
});
