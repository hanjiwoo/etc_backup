# def solution(answers):
def solution():
	answers=[1,3,2,4,2]
	
	answer = []

	one=[1,2,3,4,5]
	two=[2,1,2,3,2,4,2,5]
	three=[3,3,1,1,2,2,4,4,5,5]

	r=[0,0,0]

	one_len=len(one)
	two_len=len(two)
	three_len=len(three)

	for i in range(len(answers)):
		if answers[i]==one[(i%one_len)]:
			r[0]+=1
		if answers[i]==two[(i%two_len)]:
			r[1]+=1
		if answers[i]==three[(i%three_len)]:
			r[2]+=1

	max_x=max(r)

	for i in range(len(r)):
		if r[i]==max_x : answer.append(i+1)

	print(answer)
	return answer

solution()