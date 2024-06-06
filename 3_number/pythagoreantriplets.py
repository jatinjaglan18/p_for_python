'''
1. You are required to check if a given set of numbers is a valid pythagorean triplet.
2. Take as input three numbers a, b and c.
3. Print true if they can form a pythagorean triplet and false otherwise.
'''

i = int(input())
j = int(input())
k = int(input())

#h = max(i,j,k)

m_x = i
if j > m_x:
    m_x = j

if k > m_x:             #why we don't use elif --> we have to check for all three
    m_x = k


if i == m_x :
    i = j
    j = k
    
elif j == m_x:
    j = k

s = (i**2) + (j**2)
if s == (m_x**2):
    print(True)
else: 
    print(False)