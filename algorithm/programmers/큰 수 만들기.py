def solution(number, k):
    answer=""
    length=len(number)
    cnt=0

    # for i in range(0,k):
        # for j in range(0,length-1):
        #     if(int(number[j])<int(number[j+1])):
        #         number=number[:j]+number[j+1:]
        #         break
        #     else : continue



    # if len(number)==length:
    #     answer=number[k:]
    # else :answer=number

    # for j in range(0,length-1):
    #     if cnt!=k:    
    #         if(int(number[j])<int(number[j+1])):
    #             number=number[:j]+" "+number[j+1:]
    #             cnt+=1
    #         else: number=number
    #     else : answer=number

    # answer=answer.replace(' ','')

    # if len(number)==length:
    #     answer=number[k:]
    # else :answer=number
    j=0
    for i in range(length-1):
        if cnt!=k:
            if(int(number[j])<int(number[j+1])):
                number=number[:j]+number[j+1:]
                cnt+=1
                j=j-1 if j>0 else 0
            else : 
                number=number
                j+=1
        else : 
            answer=number
            break

    if len(number)==length:
        answer=number[k:]
    else :answer=number

    return answer

a=solution("162549128",5)
print(a)