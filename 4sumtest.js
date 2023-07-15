const checkSet=(a1,a2)=>{
    temp =a2
    for(let i=0;i<a1.length;i++){
    for(let j=0;j<temp.length;j++){
        if(a1[i]===temp[j]){
            temp.splice(j,1)
        }
    }
}return temp.length===0
}
console.log(checkSet([1,0,-1,0,-2,2],[-1,-1,0,2]))