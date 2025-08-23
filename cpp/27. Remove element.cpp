class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int occurence_rate = 0;
        int vecSize = nums.size();
        int bSubArrIndex = vecSize - 1;

        for (int i = 0; ((i < vecSize) && (bSubArrIndex >= i)); i += 1) {
            if (nums[i] == val) {
                int bSubArrElem = nums[bSubArrIndex];
                while (bSubArrElem == val && bSubArrIndex > i) {
                    bSubArrIndex -= 1;
                    bSubArrElem = nums[bSubArrIndex];
                    occurence_rate += 1;
                }
                if (bSubArrIndex >= i) {
                    nums[i] = nums[bSubArrIndex];
                    nums[bSubArrIndex] = val;
                    occurence_rate += 1;
                    bSubArrIndex -= 1;
                }
            }
        }
        
        return (vecSize - occurence_rate);
    }
};


/*
    Runtime: 2ms; Beats 2.05%
    Memory: 10.37MB; Beats 100%
*/