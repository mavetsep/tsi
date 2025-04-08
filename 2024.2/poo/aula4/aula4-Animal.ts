abstract class Animal {
    nome: string;
    idade: number;

    constructor(nome: string, idade: number) {
        this.nome = nome;
        this.idade = idade;
    }

    emitirSom() {}
}

class Cachorro extends Animal {
  emitirSom() {
    console.log("Ruf")
  }

}

class Gato extends Animal {
  emitirSom() {
    console.log("Snif")
  }

}

let animais: Animal[] = [
  new Cachorro("Rex", 3),
  new Gato("Rengar", 6)
]

animais.forEach(animal => {
  console.log(animal.nome);
  animal.emitirSom()
})