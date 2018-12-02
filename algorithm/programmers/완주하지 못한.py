# def solution(participant, completion):
participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

    answer = ''
    for i in range(0,len(completion)):
    	print(completion[i])
        if completion[i] in participant:
            continue
        else : 
            answer=completion[i]
            break
            
    return answer

