var fs = require('fs');
var np = require('numjs');
var express = require('express');

var app = express();

app.use(express.static('public'));

function proccessData(data) {
    var netWeights = JSON.parse(fs.readFileSync('net.json'))['0'];
    var layers = netWeights[0];
    var layer;
    var biases = netWeights[1];
    var bias;
    var input = np.array(data);
    var output;
    var max;

    for(var i = 0; i < layers.length; i += 1) {
        layer = np.array(layers[i]);
        bias = np.array(biases[i]);
        input = np.dot(input.T, layer.T).T.add(bias);
    }
    max = input.max();
    for (var i = 0; i < input.length; i += 1) {
        if(max === input[i]) output = i;
    }
    return output;
}

app.get('/', function (req, res) {
    res.sendFile('index.html');
});

app.get('/data', function (req, res) {
  var result = proccessData( JSON.parse(req.body.data) );
  res.send(result);
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});