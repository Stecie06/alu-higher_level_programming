#!/usr/bin/node
const anyArg = process.argv[2];
const newInt = Number(anyArg);
const textInput = 'C is fun';
if (isNaN(newInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < newInt; i++) {
    console.log(textInput);
  }
}
