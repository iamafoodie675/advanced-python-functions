l1=[1,2,3,4,5,6,7,9,10]

even = [i for i in l1 if i%2 ==0]

print(even)

#=================================

n1 =[1,2,3]
n2 =[4,5,6]

sum =map(lambda x,y: x+y ,n1,n2)

print(list(sum))


#====================================

def sq(n):
    return n*n

num =[2,3,4,5,6,7,8,9,500]

square =list(map(sq,num))
print(square)
