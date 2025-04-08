abstract class FormaGeometrica {
    protected base: number;
    protected altura: number;
   
    constructor(base: number, altura: number) {
        this.base = base;
        this.altura = altura;
    }
   
    calcularArea() {
   
    }
}

class Retangulo extends FormaGeometrica {
    calcularArea() {
        console.log(this.base * this.altura);
    }
}

class Triangulo extends FormaGeometrica {
    calcularArea() {
        console.log((this.base * this.altura)/2);
    }
}

let r: FormaGeometrica = new Retangulo(3, 4);
r.calcularArea();

let t: FormaGeometrica = new Triangulo(3, 4);
t.calcularArea();