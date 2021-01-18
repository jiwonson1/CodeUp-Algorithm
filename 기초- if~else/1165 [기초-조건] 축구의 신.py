time,score=map(int,input().split())

if(time%10==0):
    final_score = score + int((90-time)/5)
else:
    final_score = score + int((90-time)/5)+1

print(final_score)
