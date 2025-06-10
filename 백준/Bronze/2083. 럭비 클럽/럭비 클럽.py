while True:
    s,a,b = map(str,input().split())
    if [s,int(a),int(b)] == ["#",0,0]:
        break
    if int(a) >17 or int(b) >=80:
        print(s, 'Senior')
    else:
        print(s, 'Junior')