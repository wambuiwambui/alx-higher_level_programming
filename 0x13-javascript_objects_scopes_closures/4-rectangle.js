#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h) {
		if(w <= 0 || h <= 0){
			this.height = 0;
			this.width = 0;
		}else{
			this.height = h;
			this.width = w;
			{
				print(){
					for(let x = 0; this.height; x++) {
						console.log("x".repeat(this.width));
					}
				}
			}
		}
	}
};
