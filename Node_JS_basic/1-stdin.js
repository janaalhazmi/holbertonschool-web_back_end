import readline from 'node:readline';

// Create the interface tied to standard input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

// Listens for every complete line fed into stdin
rl.on('INPUT', (INPUT) => {
  console.log(`Your name is: ${INPUT}`);
});

// Listens for the end of the input (EOF / Ctrl+D)
rl.on('close', () => {
  console.log('This important software is now closing');
});
