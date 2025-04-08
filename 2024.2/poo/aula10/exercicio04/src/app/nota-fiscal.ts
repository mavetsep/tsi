import { ItemNotaFiscal } from "./item-nota-fiscal";

export class NotaFiscal {

    itens: ItemNotaFiscal[] = [];

    constructor (
        public numero: number,
        public cliente: string, 
        public enderecoEntrega: string
    ) {}

    adicionarItem(item: ItemNotaFiscal) {
        this.itens.push(item);
    }

    removerItem(indice: number) {
        this.itens.splice(indice, 1);
    }

    calcularTotal() {
        return this.itens.reduce((somatorio, item) => somatorio + item.subTotal(), 0);
    }
}
