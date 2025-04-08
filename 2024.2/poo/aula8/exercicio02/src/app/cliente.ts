import { Animal } from './animal';

export class Cliente {
  nome: string;
  email: string;
  telefone: string;
  dataCadastro: Date;
  animais: Animal[] = [];

  constructor(
    nome: string,
    email: string,
    telefone: string,
    dataCadastro: Date
  ) {
    this.nome = nome;
    this.email = email;
    this.telefone = telefone;
    this.dataCadastro = dataCadastro;
  }

  adicionarAnimal(animal: Animal) {
    if (this.animais.length < 5) {
      this.animais.push(animal);
    } else {
      throw new Error('Um cliente só pode ter, no máximo, cinco animais.');
    }
  }
}
