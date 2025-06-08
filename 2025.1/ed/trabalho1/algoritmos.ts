export function bubbleSort<T>(arr: T[]): T[] {
    const n = arr.length;
    let swapped: boolean;
    do {
      swapped = false;
      for (let i = 1; i < n; i++) {
        if (arr[i - 1] > arr[i]) {
          [arr[i - 1], arr[i]] = [arr[i], arr[i - 1]];
          swapped = true;
        }
      }
    } while (swapped);
    return arr;
}

export function selectionSort<T>(arr: T[]): T[] {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIdx]) {
        minIdx = j;
      }
    }
    if (minIdx !== i) {
      [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
    }
  }
  return arr;
}

export function insertionSort<T>(arr: T[]): T[] {
  for (let i = 1; i < arr.length; i++) {
    const key = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
  return arr;
}

export function stoogeSort(arr: number[], inicio: number, fim: number): void {
  // Se o primeiro elemento for maior que o último, troca-os
  if (arr[inicio] > arr[fim]) {
    [arr[inicio], arr[fim]] = [arr[fim], arr[inicio]]; // Swap
  }
  // Se houver 3 ou mais elementos no sub-array
  if (fim - inicio + 1 > 2) {
    const t = Math.floor((fim - inicio + 1) / 3);
    // 1. Ordena recursivamente os primeiros 2/3 do array
    stoogeSort(arr, inicio, fim - t);
    // 2. Ordena recursivamente os últimos 2/3 do array
    stoogeSort(arr, inicio + t, fim);
    // 3. Ordena novamente os primeiros 2/3 para garantir a ordem final
    stoogeSort(arr, inicio, fim - t);
  }
}

export function gnomeSort<T>(arr: T[]): T[] {
  let index = 0;
  const n = arr.length;
  while (index < n) {
    if (index === 0 || arr[index] >= arr[index - 1]) {
      index++;
    } else {
      [arr[index], arr[index - 1]] = [arr[index - 1], arr[index]];
      index--;
    }
  }
  return arr;
}