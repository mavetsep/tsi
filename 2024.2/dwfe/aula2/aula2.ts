class Aluno {
    matricula: number;
    nome: string;
    isMatriculado : boolean | null;

    constructor(matricula : number, nome : string, isMatriculado : boolean) {
        this.nome = nome;
        this.matricula = matricula;
        this.isMatriculado = true;
    }

    relatorioDados() : string {
        return "Matricula: " + this.matricula + ", Nome: " + this.nome;
    }

    nomeNVezes(vezes: Number) : string {
        let result : string = "";

        for(let index = 0, index <= vezes; index + 1) {
            
        }

        return result;
    }
}

let aluno : Aluno = new Aluno(12, "Lucas", true);

console.log(aluno.relatorioDados())