# def solution(participant, completion):
#     answer = ''
#     for i in range(0,len(completion)):
#         if completion[i] in participant:
#             continue
#         else : 
#             answer=completion[i]
#             break
            
#     return answer

# participant=["leo", "kiki", "eden"]
# completion=["eden", "kiki"]
# 

def solution(participant, completion):
	answer = ''
	tmp=0
	res={}

	for par in participant:
		res[hash(par)]=par
		tmp+=hash(par)

	for com in completion:
		tmp-=hash(com)

	answer=res[tmp]
	print(answer)
	return answer

# 해시,,,,,,,,

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]  
#participant=["mislav", "stanko", "mislav", "ana"]
#completion=["stanko", "ana", "mislav"]

solution(participant,completion)