#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // böyükdən kiçiyə
  let second = args[1];

  // handle duplicate max values
  for (let i = 0; i < args.length; i++) {
    if (args[i] < args[0]) {
      second = args[i];
      break;
    }
  }

  console.log(second);
}
