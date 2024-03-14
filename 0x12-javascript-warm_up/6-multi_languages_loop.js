#!/usr/bin/node
const myLines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

// Existing lines
const existingLines = myLines.length;
let i = 0;
while (i < existingLines) {
	console.log(myLines[i]);
	i++;
}

// Additional lines if necessary
const additionalLines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const missingLines = additionalLines.length - existingLines;
i = 0;
while (i < missingLines) {
	console.log(additionalLines[i]);
	i++;
}

