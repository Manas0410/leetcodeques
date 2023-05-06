var areDeeplyEqual = function (o1, o2) {
    if (
        typeof o1 !== "object" || typeof o2 !== "object" ||  o1 === null || o2 === null ||  Array.isArray(o1) !== Array.isArray(o2)
      ) {
        return false;
      }
      if(Array.isArray(o1) === Array.isArray(o2)){ //if both are array
        console.log("arcall",o1,o2)
        if(o1.length !== o2.length){
            return false
        }
        for(let i=0;i<o1.length;i++){
            if(typeof o1[i]!== typeof o2[i]){
                return false
            }
            if (typeof o1[i] === "object" && typeof o2[i] === "object"){
              if (!areDeeplyEqual(o1[key], o2[key])) {
                return false;
              }
            }
            if (o1[i]===o2[i]){
                return false
            }
        }return true
          }
  for (let key in o1) {
    if (o2.hasOwnProperty(key)) {
        console.log(o1[key],o2[key])
        if (typeof o1[key] === "object" && typeof o2[key] === "object") {
      if (!areDeeplyEqual(o1[key], o2[key])) {
        return false;
      }
    }
      if (o1[key] !== o2[key]) {
        return false;
      }
    }
  }
  return true;
};
console.log(areDeeplyEqual({"x":null,"L":[1,2,3]},{"x":null,"L":["1","2","3"]}))