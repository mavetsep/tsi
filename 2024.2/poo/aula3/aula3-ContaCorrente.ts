class ContaCorrente {
    numero: number;
    titular: string;
    saldo: number;
    
    constructor(
      aNumero: number,
      aTitular: string,
      aSaldo: number) {
        this.numero = aNumero;
        this.titular = aTitular;
        this.saldo = aSaldo;
    }
    
    depositar(valor: number) {
        this.saldo += valor;
    }
    
    sacar(valor: number) {
        this.saldo -= valor;
    }
    
    exibirSaldo() {
        console.log(this.saldo)
    }
    
  }

  const conta = new ContaCorrente(1, "Lucas", 0)