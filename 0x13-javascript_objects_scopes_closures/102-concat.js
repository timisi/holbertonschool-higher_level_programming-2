#!/usr/bin/node

let finalData = '';
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;

  const dataFile1 = data.toString();
  finalData += dataFile1;
});

fs.readFile(process.argv[3], (err, data) => {
  if (err) throw err;

  const dataFile2 = data.toString();
  finalData += dataFile2;
  const fs2 = require('fs');
  fs2.writeFile(process.argv[4], finalData, (err) => {
    if (err) throw err;
  });
});
