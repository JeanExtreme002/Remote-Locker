const router = require("./route/routes");
const express = require("express");
const bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.use(router);

const PORT = process.env.PORT || 5000;

app.use(express.static("static"));

app.listen(PORT, function(){
    console.log(`Running server on port ${PORT}`);
});
