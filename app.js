// simpan dengan nama app.js
const express = require("express");
const app = express();

// route utama
app.get("/", (req, res) => {
  res.send("Hello, server express berjalan tanpa rate limit!");
});

// contoh route tambahan
app.get("/about", (req, res) => {
  res.send("Ini halaman About tanpa rate limit.");
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server express berjalan di http://localhost:${PORT}`);
});
