#include <stdio.h>

int main(){
	int N;
	int K;
	int coin[10];
	int i=0;
	int max_i=0;
	int g=0;
	
	scanf("%d %d",&N,&K);
	
	for(i=0;i<N;i++){
		scanf("%d",&coin[i]);
		if(coin[i]<K) max_i=i; 
	}
	
	for(i=max_i;K>0;i--){
		g+=K/coin[i];
		K=K%coin[i];	
	}
	
	printf("%d",g);
}
