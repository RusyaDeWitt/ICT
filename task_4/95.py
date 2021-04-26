def license_gen():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = [1,2,3,4,5,6,7,8,9,0]
    length = rand.randint(3,4)
    licen_numbs = rand.sample(numbers,length)
    licen_letts = rand.sample(letters,3)
    licen = ''
    if length == 3:
        for i in licen_letts:
            licen = licen + i
        for i in licen_numbs:
            licen = licen + str(i)
    elif length == 4:
        for i in licen_numbs:
            licen = licen + str(i)
        for i in licen_letts:
            licen = licen + i
    print(licen)
    return licen


license_gen()
