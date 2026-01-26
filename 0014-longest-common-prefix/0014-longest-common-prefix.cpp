class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       string a=strs[0];
       for(string b:strs){
        string answ="";
        
        for(int i=0;i<b.size()&&i<a.size();i++){
            if(b[i]==a[i]){
                 answ+=a[i];
                 continue;
                 
            }
            
            break;
            
            }
            a=answ;
        }
       
       return a;
    }
};