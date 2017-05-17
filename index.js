var fs = require('fs');
var np = require('numjs');
var express = require('express');
var bodyParser = require('body-parser')

//var netWeights = JSON.parse(fs.readFileSync('net.json'))['0'];
//var layers = netWeights[0];
//var biases = netWeights[1];

var app = express();

app.use(express.static('public'));

app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

function proccessData(data, res) {
    const exec = require('child_process').exec;
    exec('python neural.py ' + JSON.stringify({'\"data\"': data}), (err, stdout, stderr) => {
        if (err) {
            console.error(err);
            return;
        }

        var resArray = JSON.parse(stdout)[0];
        var result = resArray.reduce((iMax, x, i, arr) => x > arr[iMax] ? i : iMax, 0);

        res.json({number: result, array: resArray});
    });
    // var layer;
    // var bias;
    // var input = np.array(data);
    // var output;
    // var max;

    // input = input.reshape(1, input.shape[0]);
    // for(var i = 0; i < layers.length; i += 1) {
    //     layer = np.array(layers[i]);
    //     bias = np.array(biases[i]);
    //     input = np.dot(input, layer.T).T.add(bias).T;
    // }
    // max = input.max();
    // input = input.tolist()[0];
    // console.log(input);
    // for (var i = 0; i < input.length; i += 1) {
    //     if(max === input[i]) output = i;
    // }
    // console.log(output)
    // return output;
}

app.get('/', function (req, res) {
    res.sendFile('index.html');
});

app.post('/data', function (req, res) {
  var result = proccessData( req.body.data, res);
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});