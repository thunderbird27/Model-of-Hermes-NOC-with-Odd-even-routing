i = 0 #row
j = 0 #column

no = 0 # router number

rowval = 30
colval = 30
routval = 900

routeraddr = { }
while j < colval:

   while i < colval:
      a = "ROUTER_ID_"+str(no)+"_x"
      routeraddr[a] = str(i)
      print a,i
      b = "ROUTER_ID_"+str(no)+"_y"
      routeraddr[b] = str(j)
      print b, j
      i = i + 1
      no = no + 1          
   j = j +1
   i = 0
   

filename2 ="mapad.txt"
mapad = open(filename2,'w')

for keys,itms in routeraddr.items():
    a = keys.split('_')
    print a,a[2],a[3] 

   
    data1 = "router_id_"+a[3]+"[" + a[2]+ "] = "+ keys +";"
    mapad.write(data1)
    datan = '\n'
    mapad.write(datan)

  
mapad.close()
