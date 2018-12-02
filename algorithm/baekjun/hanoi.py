def hanoi(n,From,To,For):
	if n==1: 
		print(From," ",To)
		return
	hanoi(n-1,From,For,To)
	print(From," ",To)
	hanoi(n-1,For,To,From)

N = int(input())

move_c = 2**N-1

print(move_c)

hanoi(N,1,3,2)