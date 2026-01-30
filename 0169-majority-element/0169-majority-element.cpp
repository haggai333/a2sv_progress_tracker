class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int>a;
        int lla=0;
        int g;
        for(int i:nums){
            a[i]++;
        }
        for(auto i:a){
            if(lla<i.second){
                g=i.first;
                lla=i.second;
            }
        }
        return g;
    }
};