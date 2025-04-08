// Crie uma classe base Funcionario:
// Propriedades:
// nome (string)
// salarioBase (number)

// Construtor: inicialize as propriedades nome e salarioBase.

// Método:
// calcularSalario() que retorna o salário base.

// Crie uma classe Gerente que herda de Funcionario:
// Adicione uma nova propriedade bonus (number).
// Modifique o método calcularSalario() para retornar o salário base somado ao bônus.

// Crie uma classe Vendedor que herda de Funcionario:

// Adicione uma nova propriedade comissao (number).
// Modifique o método calcularSalario() para retornar o salário base somado à comissão.

// Teste o código:
// Crie uma instância de Funcionario, Gerente e Vendedor.
// Exiba o salário de cada um usando o método calcularSalario.

class Funcionario {
  nome: string;
  salarioBase: number;
 
  constructor(nome: string, salarioBase: number) {
    this.nome = nome;
    this.salarioBase = salarioBase;
  }
 
  calcularSalario() {
     return this.salarioBase;
  }
}

class Gerente extends Funcionario { // Aqui o bônus é obrigatório
  bonus: number = 0;
  
  constructor(nome: string, salarioBase: number, bonus: number) {
  super(nome, salarioBase);
      this.bonus = bonus;
  }
  
  calcularSalario() {
     return this.salarioBase + this.bonus;
  }
}

class Vendedor extends Funcionario { // Aqui a comissão é opcional
comissao: number = 0;
  
  calcularSalario() {
     return this.salarioBase + this.comissao;
  }
}

let funcionario = new Funcionario("Lucas", 1200);
console.log("Salário: " + "R$ "+ funcionario.calcularSalario());

let gerente = new Gerente("Lucas", 2200, 300);
console.log("Salário: " + "R$ "+ gerente.calcularSalario());

let vendedor = new Vendedor("Lucas", 1500);
console.log("Salário: " + "R$ "+ vendedor.calcularSalario());
vendedor.comissao = 500
console.log("Salário: " + "R$ "+ vendedor.calcularSalario());
