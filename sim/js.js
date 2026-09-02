/*
import promptSync from 'prompt-sync';

const input = promptSync();
/*
 
const ageString = prompt("whats the age? ");
 

const age = parseInt(ageString, 10);
 

if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are not an adult yet.");
}


function ageFinder(age){
  console.log("whats you age please let me me ")

};

*/
/*
// Age finding logic as well as getting age from the user also added inside the function!!
const number_userAge = input("what is your age please?\n");

const number_ageFinder = (number_Age) => {
  let boolean_correctAnswer = false;
  while (boolean_correctAnswer =) {
    if (Number.isNaN(number_Age)) {
      return "Please enter a valid number in number format!!";
    }

  }

  if (number_Age < 0) {
    return "age cannot be negative!!";
  }
  else if (number_Age < 13) {
    return "child";
  }
  else if (number_Age < 19) {
    return "teenage";
  }
  else if (number_Age < 60) {
    return "adult";
  }
  else {
    return "senior";
  }
}

const number_main = () => {
  const number_answer = number_ageFinder(number_userAge);
  console.log(`the age is ${number_answer}`);
}

number_main();
*/

/*
const n = 3

for(let i = 1 ; i < 11 ; i++){
  if(i==5){
    continue;
  }else{
    let result = n * i ;
    console.log(`3*${i}=${result}`);
  }
}

*/
/*
let name = "hassan";
let reverseName = "" ;

for(let i=0 ; i<name.length ; i++){
   reverseName = name[i] + reverseName;
}

console.log(reverseName);


let n = 5 ;
let x = 1;

for(let i = n ; i > 0 ; i--){
  x = x*i ;
}

console.log(x);
*/

class Student{
  constructor(name, age, grade){
    this.name = name ;
    this.age =  age ;
    this.grade = grade ;
  }

  
}