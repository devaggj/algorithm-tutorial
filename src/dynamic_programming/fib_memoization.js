/*
time complexity => O(2^n)
space complexity => O(n)
*/
const dib = (n) => {
    if (n <= 1) return;
    dib(n - 1);
    dib(n - 1);
};

/*
time complexity => O(2^n)
space complexity => O(n/2) => O(n)
*/
const lib = (n) => {
    if (n <= 1) return;
    dib(n - 2);
    dib(n - 2);
};

/*
:비교: dib < fib < lib
time complexity => O(2^n)
space complexity => O(n)
*/
const fib = (n) => {
    if (n <= 2) return 1;
    return fib(n - 1) + fib(n - 2);
};

/*
개선된 fib using memoization
time complexity => O(2n) => O(n)
space complexity => O(n)
*/
const fib_new = (n, memo = {}) => {
    if (n in memo) return memo[n];
    if (n <= 2) return 1;

    memo[n] = fib_new(n - 1, memo) + fib_new(n - 2, memo);
    return memo[n];
};

console.log(fib_new(6));    // 8
console.log(fib_new(7));    // 13
console.log(fib_new(8));    // 21
console.log(fib_new(50));   // 12586269025 (too slow if use fib)
