const express = require("express");
const app = express();

var status = false;

// Rota para bloquear o dispositivo.
app.get("/lock", function(request, response){
    status = true;
    response.send("Locked");
});

// Rota principal para verificação.
app.get("/", function(request, response){
    response.send(status);
    status = false;
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, function(){
    console.log(`Running server on port ${PORT}`);
});
