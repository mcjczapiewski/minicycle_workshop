
// Run with: node adventure.js

// See https://nodejs.org/api/readline.html
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let player = {
  room: "outside",
};

let rooms = {
  outside: {
    title: "Outside",
    description: "You are standing outside of a huge cave entrance.",
  },
  cave: {
    title: "Cave",
    description: "You're in a cave.",
  },
};

function main() {
  describeRoom();
  askForCommand();
}

function describeRoom() {
  const room = rooms[player.room];
  rl.write(`\n${room.title}\n\n`);
  rl.write(`${room.description}\n`);
}

function askForCommand() {
  rl.write('\n');
  rl.question('> ', runCommand);
}

function runCommand(command) {
  let playing = true;
  switch(command) {
    case 'l':
    case 'look':
      describeRoom();
      break;

    case 'q':
    case 'quit':
      rl.write("Bye!\n");
      playing = false;
      break;

    default:
      rl.write(`Unrecognized command: ${command}\n`);
  }

  if (playing) {
    askForCommand();
  } else {
    rl.close();
  }
};

main();
