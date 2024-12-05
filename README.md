# RestApi
Python Project RestApi

<br>

<br>

Technologies Used


<br>

(1)  Python with Flask or FastAPI
<br>


(2) Flask (Python) or Express.js (Node.js).

<br>


(3) Database: PostgreSQL, SQLite, or MongoDB.
<br>

(4)  OpenAPI.
<br>


(5) Description: Overview of the API and its features.

<br>

<br>


const express = require('express'); const app = express();

app.get('/', (req, res) => {

res.send('

Hello, World!
'); });
app.listen(8000, () => {

console.log(Server is listening at http://localhost:8000); });

const express = require('express'); const app = express();

app.get('/', (req, res) => res.send('

Hello, World!
'));
app.listen(8000, () => console.log('Server listening on port 8000'));

const express = require('express'); const app = express();

app.use((req, res) => {

res.send('

Hello, World!
'); });
app.listen(8000, () => console.log('Server listening on port 8000'));