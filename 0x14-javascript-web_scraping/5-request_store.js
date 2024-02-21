#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
    } else {
        fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
            if (err) {
                console.error('Error writing to file:', err);
            }
        });
    }
});
