// recursividade
function soma1(n: number): number {
    let total = 0
    for (let i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}

// soma recursiva 
function soma2(n: number): number {
    if (n == 1) return 1; //caso base
    return n + soma2(n - 1); //chamada recursiva
}

import * as readline from 'node:readline/promises';
import { stdin, stdout } from 'node:process';
const rl = readline.createInterface({ input: stdin, output: stdout });

async function main() {
    const num = parseInt(await rl.question("Digite um número para somar de 1 até N: "));
    console.log(`Resultado da soma: ${soma2(num)}`);
    rl.close();
}

main();

// fatorial recursivo
function fatorial(n: number): number {
    if (n <= 1) return 1; //caso base
    return n * fatorial(n - 1); //chamada recursiva
}

const num = parseInt(prompt("Digite um número para calcular o fatorial: ")!);
console.log(`Fatorial de ${num} é: ${fatorial(num)}`);


// Implemente uma função recursiva que permita somar os elementos de um vetor de inteiros.
function somaVetor(vetor: number[], i: number): number {
    if (i < 0) return 0;
    return vetor[i] + somaVetor(vetor, i - 1);
}

const v = [12, 2, 31, 40, 15];
console.log(`Soma dos elementos: ${somaVetor(v, v.length - 1)}`);


// Implemente uma função contagemRegressiva(n: number) que imprime no console uma contagem de n até 0.
function contagemRegressiva(n: number): void {
    if (n < 0) return; // caso base
    console.log(n);
    contagemRegressiva(n - 1); // chamada recursiva
}