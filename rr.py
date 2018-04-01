row=1
while row<10:
    col=1
    while col<=row:
        print(str(col)+"*"+str(row)+"="+str(row*col),end="\t")
        col+=1
    print("")
    row+=1    