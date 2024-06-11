# Restapi
This is my second Git Repository.
<br>
Author- Kamal nayan choubey

const express = require('express');
const app = express();
 

app.get('/', (req, res) => {

  res.send('<h1> Hello, World! </h1>');
});
 
app.listen(8000, () => {

  console.log(`Server is listening at http://localhost:8000`);
});


const express = require('express');
const app = express();
 

app.get('/', (req, res) => res.send('<h1>Hello, World!</h1>'));
 

app.listen(8000, () => console.log('Server listening on port 8000'));


const express = require('express');
const app = express();
 
app.use((req, res) => {

  res.send('<h1>Hello, World!</h1>');
});
 

app.listen(8000, () => console.log('Server listening on port 8000'));
