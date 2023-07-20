var minSubArrayLen = function(target, nums) {
    left =0
    total = 0
    res = Infinity
    for (let i = 0 ; i<nums.length ;i++){
        total += nums[i]
        while (total>=target){
            res = Math.min(res,i-left+1)
            total-=nums[left]
            left+=1
        }
    }
    return res === Infinity ? 0:res
};