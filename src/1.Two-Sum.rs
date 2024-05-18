use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let cnt = 0;
        let mut map = HashMap::new();
        for (idx, num) in nums.iter().enumerate() {
            let complement = target - num;
            if map.contains_key(&complement) {
                return vec![map.get(&complement).copied().unwrap_or(0), idx as i32]
            }
            
            map.insert(num, idx as i32);
        }

        return vec![0, 0];
    }
}
