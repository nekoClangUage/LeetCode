class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        vector<int> my_results;
        for(int i = 0; i < nums.size(); i += 1){
            for(int j = (i + 1); j < nums.size(); j += 1){
                if(nums[i] + nums[j] == target){
                    my_results.push_back(i);
                    my_results.push_back(j);
                }
            }
        }
        return my_results;
    }
};