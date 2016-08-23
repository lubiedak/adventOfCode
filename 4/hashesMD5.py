import md5


startsWith = "000000"

i = 0
while(True):
    base = "bgvyzdsv" + str(i)
    m = md5.new(base)
    hash = m.hexdigest()
    if(hash.find(startsWith) == 0):
        print(i)
        break
    
    i+=1