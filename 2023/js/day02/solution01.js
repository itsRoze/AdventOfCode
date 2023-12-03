function solution() {
  const fs = require("fs");

  // Creating a function which takes a file as input
  const readFileLines = (filename) =>
    fs.readFileSync(filename).toString("UTF8").split("\n");

  // Driver code
  let data = readFileLines("input02.txt");
  data = data.slice(0, data.length - 1);
  let results = 0;

  for (let i = 0; i < data.length; i++) {
    let game = data[i].split(":");

    let id = parseInt(game[0].split(" ")[1]);

    let subsets = game[1].split(";");

    /**'3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green' */

    let blues = 0;
    let reds = 0;
    let greens = 0;

    for (let j = 0; j < subsets.length; j++) {
      let set = subsets[j].split(",");

      for (let l = 0; l < set.length; l++) {
        let count = set[l].trim().split(" ");
        let [num, color] = count;

        if (color === "blue") {
          blues = Math.max(blues, parseInt(num));
        } else if (color === "red") {
          reds = Math.max(reds, parseInt(num));
        } else if (color === "green") {
          greens = Math.max(greens, parseInt(num));
        }
      }
    }

    if (blues <= 14 && greens <= 13 && reds <= 12) {
      results += id;
    }
  }

  return results;
}

console.log(solution());
