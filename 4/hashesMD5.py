import md5


startsWith = "000000"

i = 0
while(True):
    base = "bgvyzdsv" + str(i)
    m = md5.new(base)
    generatedHash = m.hexdigest()
    if(generatedHash.find(startsWith) == 0):
        print(i)
        break
    
    i+=1
