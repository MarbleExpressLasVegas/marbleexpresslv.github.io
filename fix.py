c = open('Container_Dashboard.html','r',encoding='utf-8').read()
c = c.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js">function checkPW', '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script><script>function checkPW')
open('Container_Dashboard.html','w',encoding='utf-8').write(c)
print('Fixed')
