#!/usr/bin/node

const rect = new Rectangle(3, 4);
module.exports = class Rectangle{
  constructor(w, h){
    if (w <=- 0 || h <=- 0){
      this.width = 0;
      this.height = 0;
    }{
      this.width = w;
      this.height = h;
    }
  }

    print(){
      for(x = 0; x < this.height; x++){
        console.log('x'.repeat(this.width))
      
      }
    }

    rotate(){
      tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }

    double(){
      result = this.width*2
      result = this.height* 2
    }
  
};
