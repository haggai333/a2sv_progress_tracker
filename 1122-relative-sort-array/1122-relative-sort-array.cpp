class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int,int>a;
        for(int i=0;i<arr1.size();i++){
                a[arr1[i]]++;
        }arr1.clear();
        for(int j=0;j<arr2.size();j++){
            for(int i=0;i<a[arr2[j]];i++){
                arr1.push_back(arr2[j]);
            }
            a.erase(arr2[j]);
        }
             for (auto &[key, count] : a) {
            for (int i = 0; i < count; i++) {
                arr1.push_back(key);
            }
        } 
        return arr1;
        

        }
    
};