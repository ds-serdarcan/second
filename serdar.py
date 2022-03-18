def count_pairs_int(diff, n_max):
    c1, c2, final = 0, 0, 0
    for num in range(2,n_max-diff):
      if num <= 400:      
        for j in range(1,num+diff+1):
          if (num+diff) % j == 0:
              c1 += 1    
          if num % j == 0: 
              c2 += 1
        if c1 == c2:
          final += 1 
        c1, c2 = 0, 0
      else:
          a ,b = 0, 0
          x = [num+1,int((num/2)+3),int((num/3)+3),int((num/4)+3),int((num/5)+3),int((num/6)+3),int((num/7)+3),int((num/8)+3),\
               int((num/9)+3),int((num/10)+3),int((num/11)+3),int((num/12)+3)]
          for i in x:
            for j in range(i-5,i):
              if num % j == 0:
                a += 1
          for y in range(1,i-5):
            if num % y == 0:
                a += 1
          if a>=b:      
            x = [num+diff+1,int(((num+diff)/2)+3),int(((num+diff)/3)+3),int(((num+diff)/4)+3),int(((num+diff)/5)+3),\
                  int(((num+diff)/6)+3),int(((num+diff)/7)+3),int(((num+diff)/8)+3),int(((num+diff)/9)+3),int(((num+diff)/10)+3),\
                  int(((num+diff)/11)+3),int(((num+diff)/12)+3)]
            for i in x:
                for j in range(i-5,i):
                  if (num+diff) % j == 0:
                    b += 1
            for y in range(1,i-5):
                if (num+diff) % y == 0:
                    b += 1
            if a == b:
                final += 1 
          a, b = 0, 0
    return final

import time
start = time.time()
print(count_pairs_int(6,19175))
end = time.time()
print(end-start)
