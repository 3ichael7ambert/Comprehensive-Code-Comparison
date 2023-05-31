
`javascript.js`:

// Hello, World!
console.log("Hello, JavaScript!");

// Variables
let name = "John";
console.log(name);

name = "Jane";
console.log(name);

// Manipulation
let first_name = "John";
let last_name = "Doe";
let full_name = first_name + " " + last_name;
console.log(full_name);

let x = 10;
let y = 5;
let sum = x + y;
let difference = x - y;
let product = x * y;
let quotient = x / y;
let remainder = x % y;
console.log(sum, difference, product, quotient, remainder);

// Objects and Properties
let person = {
  name: "John",
  age: 30,
  city: "New York",
};
console.log(person.name);
console.log(person.age);
person.age = 35;
person.occupation = "Engineer";
for (let key in person) {
  console.log(key, person[key]);
}

// Arrays
let fruits = ["apple", "banana", "orange"];
console.log(fruits[0]);
console.log(fruits.slice(1, 3));
fruits.push("grape");
fruits.unshift("kiwi");
fruits.splice(1, 1);
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// Calculations
let x = 10;
let y = 5;
let sum = x + y;
let difference = x - y;
let product = x * y;
let quotient = x / y;
let remainder = x % y;
console.log(sum, difference, product, quotient, remainder);

// Classes and OOP
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
  }
}

let person = new Person("John", 30);
console.log(person.name);
console.log(person.age);
person.greet();
