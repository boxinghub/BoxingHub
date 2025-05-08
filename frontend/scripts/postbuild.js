// frontend/scripts/postbuild.js
const fs   = require("fs");
const path = require("path");

// where React spits its build
const BUILD = path.resolve(__dirname, "..", "build");
// target dirs in your Django project
const STATIC_TARGET   = path.resolve(__dirname, "..", "..", "static", "dashboard");
const TEMPLATES_TARGET = path.resolve(__dirname, "..", "..", "templates", "dashboard");

// 1) copy hashed assets into static/dashboard
fs.rmSync(STATIC_TARGET, { force: true, recursive: true });
fs.mkdirSync(STATIC_TARGET, { recursive: true });
fs.readdirSync(path.join(BUILD, "static")).forEach(type => {
  fs.cpSync(
    path.join(BUILD, "static", type),
    path.join(STATIC_TARGET, type),
    { recursive: true }
  );
});

// 2) read build/index.html and rewrite it
let html = fs.readFileSync(path.join(BUILD, "index.html"), "utf8");

// inject load static at top
html = `{% load static %}\n` + html

  // CSS lines stay the same
  .replace(
    /<link href="\/static\/css\/(.+?)\.css"/g,
    `<link href="{% static 'dashboard/css/$1.css' %}" rel="stylesheet"`
  )

  // JS: match <script [any attrs] src="/static/js/...js" [any attrs]></script>
  .replace(
    /<script\b([^>]*)\s+src="\/static\/js\/(.+?\.js)"([^>]*)><\/script>/g,
    `<script$1 src="{% static 'dashboard/js/$2' %}"$3></script>`
  );


// 3) write into templates/dashboard/index.html
fs.rmSync(TEMPLATES_TARGET, { force: true, recursive: true });
fs.mkdirSync(TEMPLATES_TARGET, { recursive: true });
fs.writeFileSync(path.join(TEMPLATES_TARGET, "index.html"), html);
