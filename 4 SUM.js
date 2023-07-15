var fourSum = function(nums, target) {
    if(nums.length <4){
      return []
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
      const checkSet=(a1,a2)=>{
      temp =[...a2]
      for(let i=0;i<a1.length;i++){
      for(let j=0;j<temp.length;j++){
          if(a1[i]===temp[j]){
              temp.splice(j,1)
          }
      }
  }return temp.length===0
  }
  for(let i=res.length-1;i>=0;i--){
    if (!checkSet(nums,res[i])){
      res.splice(i,1)
    }
  }
      return res;
    };
    