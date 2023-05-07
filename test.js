function check(o1,o2){
if(Array.isArray(o1) === Array.isArray(o2)){ //if both are array
    console.log("arcall",o1,o2)
    if(o1.length !== o2.length){
        return false
    }
    for(let i=0;i<o1.length;i++){
        if(typeof o1[i] !== typeof o2[i]){
            return false
        }
        
        
        if (o1[i]!==o2[i]){
            return false
        }}
    return true}}
console.log(check([1,2,3],[1,2,3]))