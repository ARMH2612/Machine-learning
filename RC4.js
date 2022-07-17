let swap = (i,j,S)=>{
    let temp = S[i]
    S[i] = S[j]
    S[j] = temp
}

// Initialisation : 
let K = [18,8,8] //=> 18 = S, I = 8, I = 8
let S = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
let T = [18,8,8,18,8,8,18,8,8,18,8,8,18,8,8]

// Permutation:
let j = 0;
for (let i = 0; i < 15; i++) {
    j = (j + S[i] + T[i]) % 15;
    swap(i,j,S)
}

i=0, j = 0;
let t = 0;
let k = 0;
let cipher= [];
let message= [17,0,7,8,2,7,4]
let counter = 0;
while (true) {
 i = (i + 1) % 8;
 j = (j + S[i]) % 8;
 swap (i, j,S);
 console.log("S ",S);
 t = (S[i] + S[j]) % 8;
 k = S[t]; 
 console.log("i = "+i+" | j = "+j+" | k = "+k+" | t = "+t+" | S[i] = "+S[i]+" | S[j] = "+S[j]);

 // performe XOR:
 
 if(counter>=message.length){
     break
 }
cipher.push(k ^ message[counter])
counter ++;
} 

// for (let index = 0; index < message.length; index++) {
//     cipher.push(k[index]^message[counter[index]]);
    
// }
console.log(cipher);
