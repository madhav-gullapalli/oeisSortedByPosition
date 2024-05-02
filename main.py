file2 = open("textDB","w+")
file1 = open("oeis1000.txt","r+")
funcs = file1.readlines()
funcs = [x.split(' ,') for x in funcs]
cmn = {}
for f in funcs:
    print(f)
    if(len(f) > 1):
        nums = f[1].split(',')
        for i in range(len(nums)):
            if nums[i] not in cmn:
                cmn[nums[i]] = [[f[0],i]]
            else:
                cmn[nums[i]].append([f[0],i])
file1.close()
for vala in cmn:
    print(vala)
    file2.write(f'{vala} ,')
    for k in range(len(cmn[vala])):
        file2.write(f'({cmn[vala][k][0]}, {cmn[vala][k][1]}),')
    file2.write('\n')
file2.close()