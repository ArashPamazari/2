sec = int(input('sanie mored nazar ra vared konid: '))

hour = sec // 3600
sec %= 3600
minutes = sec // 60
sec %= 60


print( hour ,':' ,minutes ,':', sec)

