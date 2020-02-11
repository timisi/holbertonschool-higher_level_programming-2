#!/usr/bin/node

const request = require('request');
const urlApi = process.argv[2];

request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error); // Print the error if one occurred
  } else {
    const jsonObj = JSON.parse(body).results;
    const wedgeUrl = 'https://swapi.co/api/people/18/';
    let count = 0;
    for (let i = 0; i < jsonObj.length; i++) {
      if (jsonObj[i].characters.includes(wedgeUrl)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
