// condicionais if

let idade : number = 18
if (idade >= 18) {
    console.log("Você é maior de idade e já pode ser preso")
}
console.log("Terminou!")


function max(...numeros: number[]): number {
    let maior = numeros[0];
    for (let i = 1; i < numeros.length; i++) {
        if (numeros[i] > maior) {
            maior = numeros[i];
        }
    }
    return maior;
}

