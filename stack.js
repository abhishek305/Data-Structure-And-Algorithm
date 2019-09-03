class Stack{
    constructor(){
        this.items=[]
    }

    push(element){
        return this.items.push(element);
    }
    pop(){
        return this.items.pop();
    }
    top(){
        return this.items.length-1;

    }
    isEmpty(){
        return this.items.length ==0;
    }
    displaystack(){
       
        return this.items;
    }

}

let ex = new Stack();

console.log(ex.push(5));


console.log("top",+ex.top());

console.log(ex.displaystack());
