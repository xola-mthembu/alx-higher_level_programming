#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments
function findSecondBiggest (args) {
  if (args.length <= 3) { // Check if there are fewer than 2 numeric arguments
    return 0;
  }

  const numbers = args.slice(2).map(Number); // Convert arguments to numbers, excluding the first two
  const uniqueNumbers = [...new Set(numbers)]; // Remove duplicates and convert back to array
  uniqueNumbers.sort((a, b) => a - b); // Sort numbers in ascending order

  if (uniqueNumbers.length < 2) { // If there's less than two unique numbers, return 0
    return 0;
  } else {
    return uniqueNumbers[uniqueNumbers.length - 2]; // Return the second biggest number
  }
}

const args = process.argv;
console.log(findSecondBiggest(args));
