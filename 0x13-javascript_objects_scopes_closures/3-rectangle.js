#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
        this.width = w;
        this.height = h;
      }
    }
  }
  print(){
    for(let i = 0 ; i < h ; i++){
        console.log('X'.repeat(w));
    }
  }
  
  module.exports = Rectangle;
  