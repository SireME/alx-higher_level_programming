#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const numbers = args.map(Number); // Convert input strings to numbers
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sort in descending order
  const secondLargest = sortedNumbers[1]; // Get the second largest number

  console.log(secondLargest || 0); // Output the result or 0 if no valid input
}
