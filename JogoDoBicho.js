let bicho = [
    "Avestruz",
    "Águia",
    "Burro",
    "Borboleta",
    "Cachorro",
    "Cabra",
    "Carneiro",
    "Camelo",
    "Cobra",
    "Coelho",
    "Cavalo",
    "Elefante",
    "Galo",
    "Gato",
    "Jacaré",
    "Leão",
    "Macaco",
    "Porco",
    "Pavão",
    "Peru",
    "Touro",
    "Tigre",
    "Urso",
    "Veado",
    "Vaca",
]

const NumeroAletorio = (min, max) => Math.floor(Math.random() * (min, max + 1)) + min;

const BichoAleatorio = () => bicho[NumeroAletorio(0, bicho.length - 1)];




console.log("\nMilhar:\n" + Math.floor(Math.random() * 9999));
console.log("\nO Bicho é:\n" + BichoAleatorio());
