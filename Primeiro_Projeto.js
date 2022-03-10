console.log(`Este projeto foi criado com a proposta de registrar meus avanços e conhecimentos de programação em JavaScript, conforme aprendizado irei atualizando`);
//console.log() é usado para exibir algo na tela do computador, é utilizado ",' e `!

//A seguir irei registrar a maneira de criar Blocos, para isso é utilizado o {}, junto aos bloco, será apresentado o const, var e let.
{
    var nome = "Arroz"; /* -> o uso do "" torna o Arroz uma string. "Strings são cadeias de caracteres que armazenam dados textuais e, 
portanto, podem armazenar informações para as mais diversas finalidades. **Retirado do Google** */
    var medida = "Kg";
    var peso = 1;
    var preco = 5.90;
 }
 
console.log("Produto:" + " " + nome);
console.log("Peso:" + " " + peso + medida);
console.log("R$" + preco);

//Seguindo com o aprendizado do const, let, vet;
let a = 5; //let é uma variável, por isso, é pode ser alterado pelo =.
vet b = 10; //vet também é uma variável e de função semelhante ao let, portanto, podemos usar um ou outro conforme a preferência.
console.log(a);
console.log(b);
b = 20; //aqui o valor de b será alterado.
console.log(b);
const c = 5; //por ser uma constante, não permite alteração por meio do "="
console.log(c);
 
if(a >= 4) {
    console.log(true); //Numa leitura básica, if(Se) a variável A for maior ou igual a 4 apresentar na tela o True.
) else {               //else (Se não) apresentar False na tela.
    console.log(false);
} 
