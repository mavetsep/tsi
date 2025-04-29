// // recursividade
// function soma1(n: number): number {
//     let total = 0
//     for (let i = 1; i <= n; i++) {
//         total += i;
//     }
//     return total;
// }

// // soma recursiva 
// function soma2(n: number): number {
//     if (n == 1) return 1; //caso base
//     return n + soma2(n - 1); //chamada recursiva
// }

// import * as readline from 'node:readline/promises';
// import { stdin, stdout } from 'node:process';
// const rl = readline.createInterface({ input: stdin, output: stdout });

// async function main() {
//     const num = parseInt(await rl.question("Digite um número para somar de 1 até N: "));
//     console.log(`Resultado da soma: ${soma2(num)}`);
//     rl.close();
// }

// main();

// // fatorial recursivo
// function fatorial(n: number): number {
//     if (n <= 1) return 1; //caso base
//     return n * fatorial(n - 1); //chamada recursiva
// }

// const num = parseInt(prompt("Digite um número para calcular o fatorial: ")!);
// console.log(`Fatorial de ${num} é: ${fatorial(num)}`);






// exercicios

// 1 
// function somaVetor(vetor: number[], i: number): number {
//     if (i < 0) return 0;
//     return vetor[i] + somaVetor(vetor, i - 1);
// }

// const v = [12, 2, 31, 40, 15];
// console.log(`Soma dos elementos: ${somaVetor(v, v.length - 1)}`);


// // 2 
// function contagemRegressiva(n: number): void {
//     if (n < 0) return; // caso base
//     console.log(n);
//     contagemRegressiva(n - 1); // chamada recursiva
// }


// // 3 
// function potencia(base: number, expoente: number): number {
//     if (expoente === 0) return 1; // caso base
//     return base * potencia(base, expoente - 1); // chamada recursiva
// }

// // 4 
// function mdc(n1: number, n2: number): number {
//     if (n2 === 0) return n1; // caso base
//     return mdc(n2, n1 % n2); // chamada recursiva
// }

// // 5 
// function multiplicacao(n1: number, n2: number): number {
//     if (n2 === 0) return 0; // caso base
//     return n1 + multiplicacao(n1, n2 - 1); // chamada recursiva
// }

// // 6 
// function decimalParaBinario(n: number): string {
//     if (n === 0) return ""; // caso base
//     return decimalParaBinario(Math.floor(n / 2)) + (n % 2).toString(); // chamada recursiva
// }

// // 7 
// function mmc(n1: number, n2: number): number {
//     return (n1 * n2) / mdc(n1, n2); // usando a relação entre MMC e MDC
// }

// // 8 
// function ehPalindromo(palavra: string): boolean {
//     if (palavra.length <= 1) return true; // caso base
//     if (palavra[0] !== palavra[palavra.length - 1]) return false; // comparação
//     return ehPalindromo(palavra.slice(1, -1)); // chamada recursiva
// }

function fibonacci(n: number, memo: { [key: number]: number} = {}): number {
    if (n <= 1) {
        return n;
    }
    
    if (memo[n] !== undefined) {
        console.log(`valor ja calculado para ${n}: ${memo[n]}`);
        return memo[n];
    }

    console.log(`calculando fibonacci de ${n}`);
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}

// exemplos de uso:

const numero = 10;
console.log(`Fibonacci de ${numero} é: ${fibonacci(numero)}`); 