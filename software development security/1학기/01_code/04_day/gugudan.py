# for i in range(2,10):
# 	for j in range(1,10):
# 		print(i*j, end=" ")
# 	print('')

# list_a=[3,6,9,12]
# res1=[]
# # for n in list_a:
# # 	res1.append(n-1)
# # print(res1)

# res2=[n-1 for n in list_a]
# print(res2)

gugudan=[i*j for i in range(2,10) for j in range(1,10)]
print(gugudan)