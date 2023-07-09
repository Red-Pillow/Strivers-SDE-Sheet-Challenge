# Prob_link: https://www.codingninjas.com/studio/problems/n-queens_8230707?challengeSlug=striver-sde-challenge&leftPanelTab=0

#include <bits/stdc++.h>

using namespace std;

void solve(vector<vector<int>>&ans,vector<vector<int>>&res,vector<int>&left,vector<int>&ld,vector<int>&ud,int n,int col)

{

if(col==n)

{

vector<int>temp;

for(auto it:res)

{

for(auto j:it)

temp.push_back(j);

}

ans.push_back(temp);

return;

}

for(int row=0;row<n;row++)

{

if(left[row]==0 && ld[n-1+col-row]==0 && ud[row+col]==0)

{

left[row]=1;

ld[n-1+col-row]=1;

ud[row+col]=1;

res[row][col]=1;

solve(ans,res,left,ld,ud,n,col+1);

res[row][col]=0;

left[row]=0;

ld[n-1+col-row]=0;

ud[row+col]=0;



}

}

}

vector<vector<int>> solveNQueens(int n) {



vector<vector<int>>ans;

vector<vector<int>>res(n,vector<int>(n));

if(n>1 &&n<4)return ans;



vector<int>left(n,0);

vector<int>ud(2*n-1,0);

vector<int>ld(2*n-1,0);

solve(ans,res,left,ld,ud,n,0);

return ans;



}