"""Fix password gate - restore async/await"""
import os

PORTAL_FOLDER = r"C:\Users\meadmin\MarbleExpressPortal"
DASHBOARD = os.path.join(PORTAL_FOLDER, "Container_Dashboard.html")

with open(DASHBOARD, 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace the checkPW function
old_js = (
    "function checkPW(){"
    "const pw=document.getElementById('pw-input').value;"
    "if(pw==='Materials2026!'){"
    "sessionStorage.setItem('me_mat_auth','1');"
    "document.getElementById('pw-gate').style.display='none';}"
    "else{"
    "document.getElementById('pw-err').textContent='Incorrect password.';"
    "document.getElementById('pw-input').value='';}}"
    "if(sessionStorage.getItem('me_mat_auth')==='1'){"
    "const g=document.getElementById('pw-gate');if(g)g.style.display='none';}"
)

new_js = (
    "function checkPW(){"
    "var pw=document.getElementById('pw-input').value;"
    "if(pw==='Materials2026!'){"
    "sessionStorage.setItem('me_mat_auth','1');"
    "document.getElementById('pw-gate').style.display='none';}"
    "else{"
    "document.getElementById('pw-err').textContent='Incorrect password.';"
    "document.getElementById('pw-input').value='';}}"
    "window.onload=function(){"
    "if(sessionStorage.getItem('me_mat_auth')==='1'){"
    "var g=document.getElementById('pw-gate');if(g)g.style.display='none';}};"
)

if old_js in html:
    html = html.replace(old_js, new_js, 1)
    print("Fixed!")
else:
    # Try to find whatever is there
    idx = html.find('function checkPW')
    if idx >= 0:
        print("Found checkPW at:", idx)
        print(repr(html[idx:idx+300]))
    else:
        idx2 = html.find('checkPW')
        print("checkPW found at:", idx2)
        print(repr(html[idx2:idx2+300]))

with open(DASHBOARD, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done!")
