# Prob_link: https://www.codingninjas.com/studio/problems/count-inversions_8230680?challengeSlug=striver-sde-challenge&leftPanelTab=0

#include <bits/stdc++.h>
long long getInversions(long long *arr, int n){
    // Write your code here.
    long long c=0;

    for(int i=0;i<n;i++)

    {

        for(int j=i;j<n;j++)

        {

            if(arr[i]>arr[j])

             c++;

        }

    }

    return c;

}