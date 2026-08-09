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