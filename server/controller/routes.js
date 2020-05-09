const Locker = require("../model/locker");
const express = require("express");
const path = require('path');

const router = express.Router();
const locker = new Locker();

// Pasta pública.
router.use(express.static("public"));

// Rota principal.
router.get("/", function(request, response) {
    response.sendFile(path.resolve("templates/password.html"));
});

// Rota para obter o status do locker. (Necessário token de acesso).
router.post("/", function(request, response) {

    const token = request.body.token;

    if (locker.validate_token(request.body.token)) {
        response.send(locker.status);

    } else {
        response.sendStatus(403);
    }
});

// Rota para bloquear o dispositivo. (Necessário senha).
router.post("/lock", function(request, response) {

    const password = request.body.password;

    if (locker.lock(password)) {
        response.sendFile(path.resolve("templates/sucess.html"));

    } else {
        response.status(403);
        response.sendFile(path.resolve("templates/error.html"));
    }
});

// Rota para registrar uma nova senha. (Necessário token de acesso e uma nova senha).
router.post("/set", function(request, response) {

    const token = request.body.token;
    const new_password = request.body.password

    if (locker.set_new_password(token, new_password)) {
        response.sendStatus(200);
        
    } else {
        response.sendStatus(403);
    }
});


module.exports = router;