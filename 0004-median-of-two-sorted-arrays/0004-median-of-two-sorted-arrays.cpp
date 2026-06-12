class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    std::vector<int> a;
        for (int i = 0; i < nums1.size() ||i<nums2.size();i++) {
            if(i<nums1.size()){
            a.push_back(nums1[i]);}
            if(i<nums2.size()){
             a.push_back(nums2[i]);}
        }
      sort(a.begin(), a.end());
         if (a.size() % 2 == 0) {
            return (a[a.size() / 2 - 1] + a[a.size() / 2]) / 2.0;
        } else {
            return a[a.size() / 2];
        }
    }
};