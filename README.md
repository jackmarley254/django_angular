<h1>📚 Library Management System</h1>

<p>A full-stack web application built with <strong>Angular 20.0.2</strong> (standalone components) as the frontend and <strong>Django REST Framework</strong> as the backend. Users can <strong>add</strong>, <strong>view</strong>, and <strong>manage books</strong> with fields like Title, Author, Published Date, and ISBN.</p>

<hr />

<h2>🚀 Features</h2>
<ul>
  <li>Add new books to the library</li>
  <li>View list of all books</li>
  <li>RESTful API integration using Angular HTTPClient</li>
  <li>Standalone component architecture (Angular 17+ style)</li>
  <li>Django backend with API endpoints using DRF</li>
</ul>

<h2>🛠️ Tech Stack</h2>
<h3>Frontend:</h3>
<ul>
  <li>Angular 20.0.2</li>
  <li>SCSS or CSS</li>
  <li>TypeScript</li>
</ul>

<h3>Backend:</h3>
<ul>
  <li>Python 3.x</li>
  <li>Django 4.x</li>
  <li>Django REST Framework</li>
  <li>SQLite3 (default)</li>
</ul>

<h2>🔧 Setup Instructions</h2>

<h3>Backend (Django):</h3>
<pre>
cd django-backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
</pre>

<h3>Frontend (Angular):</h3>
<pre>
cd library-frontend
npm install
ng serve
</pre>

<p>Now visit <a href="http://localhost:4200">http://localhost:4200</a> for the Angular app, and <a href="http://localhost:8000">http://localhost:8000</a> for Django backend.</p>

<h2>🧪 Sample API Payload</h2>
<pre>
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "published_date": "08-2008",
  "isbn": "9780132350884"
}
</pre>

<h2>📬 API Endpoints</h2>
<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Endpoint</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td>/api/books/</td>
      <td>List all books</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>/api/books/</td>
      <td>Add a new book</td>
    </tr>
    <tr>
      <td>DELETE</td>
      <td>/api/books/{id}</td>
      <td>Delete a book</td>
    </tr>
  </tbody>
</table>

<h2>📦 Deployment</h2>
<ul>
  <li>Angular: Firebase Hosting, Netlify, Vercel</li>
  <li>Django: Render, Railway, DigitalOcean, or Heroku</li>
</ul>

<h2>🙌 Author</h2>
<p>Jackson Gitahi<br/>
<a href="https://www.linkedin.com/in/jackson-gitahi/">LinkedIn</a> 

<h2>📃 License</h2>
<p>MIT License — Feel free to use and modify.</p>
