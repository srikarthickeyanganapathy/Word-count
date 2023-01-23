##Developed by : Sri Karthickeyan Ganapathy
##Register number: 22008592
def program():
    count=0
    with open("new1.txt","r") as f:
        for data in f:
            words=data.split()
            for word in words:
                count+=1
    print("Total number of words:",count)
program()