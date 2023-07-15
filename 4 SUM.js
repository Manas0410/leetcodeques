var fourSum = function(nums, target) {
  if(nums.length <4){
    return []
  }
  if ([... new Set(nums)].length ===1){
    nums.splice(4,nums.length-6)
  }
   let a = [];
    let b = [];
    for (let i = 0; i < nums.length - 1; i++) {
      for (let j = i + 1; j < nums.length; j++) {
        a.push(nums[i] + nums[j]); // sum
        b.push([nums[i], nums[j]]); // values of sum
      }
    }
  
    let out = {};
    let res = [];
    let added = new Set(); // Track added quadruplets
    for (let i = 0; i < a.length; i++) {
      if ((target - a[i]) in out) {
        for (let pair of out[target - a[i]]) {
          const quadruplet = [...pair, ...b[i]].sort((a, b) => a - b); // Sort the quadruplet
          const quadrupletStr = quadruplet.join(","); // Create a string representation of the quadruplet
  
          if (!added.has(quadrupletStr)) {
            res.push(quadruplet);
            added.add(quadrupletStr);
          }
        }
      }
      if (a[i] in out) {
        out[a[i]].push(b[i]);
      } else {
        out[a[i]] = [b[i]];
      }
    }

    console.log("res:",res)
    const checkSet =(a,b)=>{
        ao={}
        bo={}
        for (let i=0;i<a.length;i++){
            ao.hasOwnProperty(a[i]) ? ao[a[i]]+=1:ao[a[i]]=1
        }
        for (let i=0;i<b.length;i++){
            bo.hasOwnProperty(b[i]) ? bo[b[i]]+=1:bo[b[i]]=1
        }
        for (let key in bo){
            if (bo[key]>ao[key]){return false}
        }
        return true
    }

for(let i=res.length-1;i>=0;i--){
  if (!checkSet(nums,res[i])){
    res.splice(i,1)
  }
}
    return res;
  };
  