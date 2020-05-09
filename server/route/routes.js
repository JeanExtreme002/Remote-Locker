const acessManager = require("../model/acessManager");
const express = require("express");
const router = express.Router();

var path = require('path');
var status = false;

// Pasta pública.
router.use(express.static("public"));


// Rota principal.
router.get("/", function(request, response){
    response.sendFile(path.resolve("templates/password.html"));
});


// Rota para verificação. ( Necessário token de acesso ).
router.post("/", function(request, response){

    if (acessManager.validateToken(request.body.token)){
        response.send(status);
        status = false;

    }else{
        response.sendStatus(403);
    }
});


// Rota para bloquear o dispositivo. ( Necessário senha ).
router.post("/lock", function(request, response){

    if (acessManager.validatePassword(request.body.password)){
        response.sendFile(path.resolve("templates/sucess.html"));
        status = true;

    }else{
        response.status(403);
        response.sendFile(path.resolve("templates/error.html"));
    }
});


// Rota para registrar uma nova senha. ( Necessário token de acesso e uma nova senha ).
router.post("/new", function(request, response){

    if (acessManager.setPassword(request.body.token, request.body.password)){
        response.sendStatus(200);
        
    }else{
        response.sendStatus(403);
    }
});


module.exports = router;