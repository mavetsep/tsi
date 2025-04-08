interface ModeloAluno {
    matricula?: number
    nome?: string
}

function LogAluno(aluno: ModeloAluno) {
    return (target: any) => {
        console.log(aluno.nome);
        console.log(aluno.matricula)
    }
}

@LogAluno({
    nome: "Lucas", 
    matricula: 123
    })

    
class Aluno {

}

let exemplo = new Aluno();