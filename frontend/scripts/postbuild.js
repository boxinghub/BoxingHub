// frontend/scripts/postbuild.js
const fs   = require("fs");
const path = require("path");

const BUILD            = path.resolve(__dirname, "..", "build");
const STATIC_TARGET    = path.resolve(__dirname, "..", "..", "static", "dashboard");
const TEMPLATES_TARGET = path.resolve(__dirname, "..", "..", "templates", "dashboard");

// 1) Copy static assets (js/, css/, manifest.json, favicon.ico, logo192.png, etc.)
fs.rmSync(STATIC_TARGET, { force: true, recursive: true });
fs.mkdirSync(STATIC_TARGET, { recursive: true });

// copy entire build/static tree
fs.cpSync(path.join(BUILD, "static"), path.join(STATIC_TARGET, "static"), { recursive: true });

// copy root-level assets
["manifest.json","favicon.ico","logo192.png","logo512.png"].forEach(file => {
  fs.copyFileSync(
    path.join(BUILD, file),
    path.join(STATIC_TARGET, file)
  );
});

// 2) Read & transform index.html
let html = fs.readFileSync(path.join(BUILD, "index.html"), "utf8");

// a) prepend the Django tag loader
html = `{% load static %}\n` + html;

// b) replace the <title> if you like
html = html.replace(
  /<title>.*<\/title>/,
  "<title>Boxer Profile</title>"
);

// c) GENERIC HREF rewrite: any href="/xxx" → {% static 'dashboard/xxx' %}
html = html.replace(
  /href="\/([^"]+)"/g,
  `href="{% static 'dashboard/$1' %}"`
);

// d) GENERIC SRC rewrite: any src="/xxx" → {% static 'dashboard/xxx' %}
html = html.replace(
  /src="\/([^"]+)"/g,
  `src="{% static 'dashboard/$1' %}"`
);

// 3) Write out the Django‐ified template
fs.rmSync(TEMPLATES_TARGET, { force: true, recursive: true });
fs.mkdirSync(TEMPLATES_TARGET, { recursive: true });
fs.writeFileSync(path.join(TEMPLATES_TARGET, "index.html"), html);
