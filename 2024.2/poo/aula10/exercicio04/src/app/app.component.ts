import { Component } from '@angular/core';
import { NotaFiscal } from './nota-fiscal';
import { FormsModule } from '@angular/forms';
import { ItemNotaFiscal } from './item-nota-fiscal';
import { CurrencyPipe } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, CurrencyPipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  notaFiscal: NotaFiscal = new NotaFiscal(0, "", "");
  itemCodigo = 0;
  itemDescricao = "";
  itemQuantidade = 0;
  itemValorUnitario = 0;
  valorTotal = 0;

  adicionarItem() {
    const itemNF: ItemNotaFiscal = new ItemNotaFiscal(
      this.itemCodigo, 
      this.itemDescricao, 
      this.itemQuantidade, 
      this.itemValorUnitario)
    this.notaFiscal.adicionarItem(itemNF);
    this.valorTotal = this.notaFiscal.calcularTotal();
  }

  removerItem(indice: number) {
    this.notaFiscal.removerItem(indice);
    this.valorTotal = this.notaFiscal.calcularTotal();
  }
}
