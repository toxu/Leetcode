#include<iostream>
#include<vector>
#include<string>
#include<unordered_set>
using namespace std;

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        unordered_set<string> queue;
        std::vector<string> res;
        queue.insert(s);
        while(true){
        	for(auto candidate: queue){
        		if(isValid(candidate)){
        		    cout<<candidate<<"in"<<endl;
        			res.push_back(candidate);
        		}
        	}
        	if(res.size() != 0){
        		return res;
        	}
        	
            unordered_set<string> t;
        	for(auto candidate: queue){
        		for(int i=0; i<candidate.size();i++){
        			string tmp = candidate.substr(0,i) + candidate.substr(i+1);
        			t.insert(tmp);
        		}
        	}
        	queue = t;
        }
    }

    bool isValid(string s){
    	int Sum = 0;
    	if(s == "") return true;
    	for(int i=0; i<s.size(); i++){
    		if(s[i] == '(')	
    			Sum++;
    		if(s[i] == ')') 
    			Sum--;
    		if(Sum < 0) 
    			return false;
    	}
    	return Sum == 0;
    }
};
int main(){
	Solution s;
	vector<string> res = s.removeInvalidParentheses(")(");
	cout<< res.size() << endl;
	for(auto c: res){
		std::cout<<c<<std::endl;
	}
}