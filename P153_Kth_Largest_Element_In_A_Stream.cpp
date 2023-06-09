# Prob_link: https://www.codingninjas.com/studio/problems/kth-largest-element-in-a-stream_8230728?challengeSlug=striver-sde-challenge&leftPanelTab=0

#include <bits/stdc++.h>
class Kthlargest {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    int K;
    Kthlargest(int k, vector<int> &arr) {
       // Write your code here.
        K = k;
        for(auto &num : arr) {
            pq.push(num);
            if(pq.size() > K)
                pq.pop();
        }
    }

    void add(int num) {
        // Write your code here.
        pq.push(num);
        if(pq.size() > K)
            pq.pop();
    }

    int getKthLargest() {
       // Write your code here.
        return pq.top();
    }

};