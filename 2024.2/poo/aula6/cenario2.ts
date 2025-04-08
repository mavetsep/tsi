// Cenário 2
// • Em uma escola, existem Professores e Disciplinas. Um professor pode lecionar várias
// disciplinas, mas cada disciplina só pode ter um professor responsável.
// • Instruções
// 1. Crie uma classe Disciplina, que possui:
// o Um atributo nome (do tipo string), que representa o nome da disciplina.
// o Um método exibirInformacoes que mostra no console o nome da
// disciplina.

// 2. Crie uma classe Professor, que possui:
// o Um atributo nome (do tipo string), representando o nome do professor.
// o Um atributo disciplinas (do tipo Disciplina[]), que é uma lista de
// disciplinas que o professor leciona.
// o Um método adicionarDisciplina que recebe uma disciplina e adiciona-a à
// lista de disciplinas do professor.
// o Um método exibirInformacoes que mostra no console o nome do
// professor e o nome de cada disciplina que ele leciona.

// 3. No código principal:
// o Crie duas instâncias de Professor chamadas professor1 e professor2.
// o Crie quatro instâncias de Disciplina e associe duas disciplinas ao
// professor1 e as outras duas ao professor2.
// o Chame o método exibirInformacoes de cada professor para exibir as
// disciplinas que ele leciona.


class Disciplina {
    nome: string;

    constructor(nome: string) {
        this.nome = nome;
    }

    exibirInformacoes() {
        console.log(this.nome)
    }
}

class Professor {
    nome: string;
    disciplinas: Disciplina[];

    constructor(nome: string) {
      this.nome = nome;
      this.disciplinas = [];
    }

    adicionarDisciplina(disciplina: Disciplina) {
      this.disciplinas.push(disciplina);
    }

    exibirInformacoes(): void {
      console.log(`Professor: ${this.nome}`);
      console.log('Disciplina(s) que leciona:');
      this.disciplinas.forEach((disciplina) => {
        disciplina.exibirInformacoes();
    });
  }
}

let disciplina1 = new Disciplina("Matemática")
let disciplina2 = new Disciplina("Química")
let disciplina3 = new Disciplina("Física")
let disciplina4 = new Disciplina("Biologia")

let professor1 = new Professor("João")
professor1.adicionarDisciplina(disciplina1)
professor1.adicionarDisciplina(disciplina3)
professor1.exibirInformacoes()

let professor2 = new Professor("Ana")
professor2.adicionarDisciplina(disciplina2)
professor2.adicionarDisciplina(disciplina4)
professor2.exibirInformacoes()
