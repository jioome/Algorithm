#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;
pair <int, int> arr[12];
int main(){
	int pen = 0;
	int cnt = 0;
	for(int i =0;i<11;i++){
		scanf("%d %d",&arr[i].first,&arr[i].second);	
	}
	sort(arr,arr+11);
	for(int i =0;i<11;i++){
		pen += cnt + arr[i].first;
		cnt += arr[i].first;
	}
	for(int i =0;i<11;i++){
		pen += (20 * arr[i].second);
	}
	printf("%d",pen);
}