# 가상의 이메일 전송 함수

def send_mail(from_mail, to_mail, subject, contents ):
	print("From: \t"+from_mail)
	print("To: \t"+to_mail)
	print("Subject: \t"+subject)
	print("*"*20)
	print(contents)
	print("*"*20)
	print("*"*20)

my_email = "jiw021538@gmail.com"

users=[]
users.append({'name':'Boo','email':'jiw021538@gmail.com'})
users.append({'name':'John','email':'jiw021538@gmail.com'}) 

contents= '''This is DSM
my leader is Eo young Bo young
i love you
'''

for user in users:
	title= 'Dear. '+user['name']
 	send_mail(my_email,user['email'],title,contents)