function factorial(n) {
 
    if (n === 0 || n === 1) {
        return 1;
    }
  
    else {
        return n * factorial(n - 1);
    }
}


let num = 5;
console.log(`The factorial of ${num} is: ${factorial(num)}`);

num = 0;
console.log(`The factorial of ${num} is: ${factorial(num)}`);

num = 10;
console.log(`The factorial of ${num} is: ${factorial(num)}`);
