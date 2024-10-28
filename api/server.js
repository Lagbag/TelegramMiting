var express = require("express");
var app = express();
var characters = require("./data/characters.json");  // Локальный JSON файл с персонажами
var spells = require("./data/spells.json");          // Локальный JSON файл с заклинаниями

// Middleware для обработки CORS (для локального тестирования CORS)
app.use("/api", function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  next();
});

// Маршрут для главной страницы
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/public/index.html");
});

// Маршрут для получения всех персонажей
app.get("/api/characters", function (req, res) {
  res.json(characters);
});

// Маршрут для получения студентов
app.get("/api/characters/students", function (req, res) {
  const students = characters.filter(character => character.hogwartsStudent);  // Предполагается, что в JSON есть поле hogwartsStudent
  res.json(students);
});

// Маршрут для получения персонала
app.get("/api/characters/staff", function (req, res) {
  const staff = characters.filter(character => character.hogwartsStaff);  // Предполагается, что в JSON есть поле hogwartsStaff
  res.json(staff);
});

// Маршрут для получения персонажей по дому
app.get("/api/characters/house/:house", function (req, res) {
  const house = req.params.house;
  const houseCharacters = characters.filter(character => character.house === house);  // Фильтрация по дому
  res.json(houseCharacters);
});

// Маршрут для получения всех заклинаний
app.get("/api/spells", function(req, res) {
  res.json(spells);
});

// Статическая папка для раздачи файлов
app.use(express.static("public"));

// Настройка порта
app.set("port", process.env.PORT || 5000);

// Запуск сервера
app.listen(app.get("port"), function() {
  console.log("Node app is running on port", app.get("port"));
});
