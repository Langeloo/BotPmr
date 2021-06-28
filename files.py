with open("Rx8.txt", "a") as f:
    for i in range(1,100000):
        p = str("Rx8-" + str(i).zfill(5) + "\n")
        f.write(p)
        print (p)

with open("Rx4.txt", "a") as g:
    for i in range(1,100000):
        p = str("Rx4-" + str(i).zfill(5) + "\n")
        g.write(p)
        print (p)

'''
for i in range(1,100000):
    p = str("Rx8-"+str(i).zfill(5))
    f.write(p)
    print (p)
'''
print("Finish!")