import { Component } from '@angular/core';
import { Cliente } from './cliente';
import { FormsModule } from '@angular/forms';
import { Animal } from './animal';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  cliente: Cliente = new Cliente('Marcelo', '', '', new Date());
  nomeAnimal = '';
  dataNascimentoAnimal = new Date();
  sexoAnimal = 'Masculino';
  especieAnimal = '';

  mensagemErro = '';

  onAdicionarAnimal() {
    let animal = new Animal(
      this.nomeAnimal,
      this.dataNascimentoAnimal,
      this.sexoAnimal,
      this.especieAnimal
    );
    // Limpar o form
    // this.nomeAnimal = '';
    // this.dataNascimentoAnimal = new Date();
    // this.sexoAnimal = 'Masculino';
    // this.especieAnimal = '';
    // Adiciona o animal a lista
    try {
      this.cliente.adicionarAnimal(animal);
    } catch(erro: any) {
     console.log(erro);
     this.mensagemErro = erro;
    }
  }
}
