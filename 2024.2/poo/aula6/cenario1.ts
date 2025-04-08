class Departamento {
  nome: string;

  constructor(nome: string) {
    this.nome = nome;
  }

  exibirInformacoes() {
    return this.nome
  }
}

class Funcionario {
  nome: string;
  departamento: Departamento;
 
  constructor(nome: string, departamento: Departamento) {
    this.nome = nome;
    this.departamento = departamento;
  }

  exibirInformacoes() {
    return this.nome
  }
 
}

let departamento1 = new Departamento("TI");
let departamento2 = new Departamento("RH");

let funcionario1 = new Funcionario("Alice", departamento1);
let funcionario2 = new Funcionario("Bruno", departamento1);
let funcionario3 = new Funcionario("Carla", departamento2);

console.log(`Funcionário: ${funcionario1.exibirInformacoes()}, Departamento: ${funcionario1.departamento.exibirInformacoes()}`)
console.log(`Funcionário: ${funcionario2.exibirInformacoes()}, Departamento: ${funcionario2.departamento.exibirInformacoes()}`)
console.log(`Funcionário: ${funcionario3.exibirInformacoes()}, Departamento: ${funcionario3.departamento.exibirInformacoes()}`)