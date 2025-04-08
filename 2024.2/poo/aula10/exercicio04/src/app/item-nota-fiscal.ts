export class ItemNotaFiscal {
    constructor (
        public codigo: number,
        public descricao: string,
        public quantidade: number,
        public valorUnitario: number
    ) {}

    subTotal() {
        return this.quantidade * this.valorUnitario;
    }
}
