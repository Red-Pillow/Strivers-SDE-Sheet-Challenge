# Prob_link: https://www.codingninjas.com/studio/problems/implement-atoi-function_8230776?challengeSlug=striver-sde-challenge&leftPanelTab=0

#include <bits/stdc++.h>

int atoi(string s) {

    // Write your code here.

    int n = s.length();

    bool neg=false;

    string  ans ="";

    for(int i=0; i<n; i++){

        if(s[i]=='-')neg=true;

        if(s[i]<65 && s[i]!='-'){

            ans = ans+s[i];

        }

    }

    //cout<<ans;

    if(neg==true)return -stoi(ans);

    return stoi(ans);



}