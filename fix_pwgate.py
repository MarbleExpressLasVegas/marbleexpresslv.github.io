"""Fix password gate in Container_Dashboard.html - use direct comparison"""
import os

PORTAL_FOLDER = r"C:\Users\meadmin\MarbleExpressPortal"
DASHBOARD = os.path.join(PORTAL_FOLDER, "Container_Dashboard.html")

with open(DASHBOARD, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the SHA256 JS with simple direct comparison
old_js = (
    "const MATERIALS_HASH='2193128112d8fac2973f3e7192ec8ac04abfddd2d3240b58ea57e0884e03027b';"
    "async function sha256(s){"
    "const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s));"
    "return Array.from(new Uint8Array(b)).map(x=>x.toString(16).padStart(2,'0')).join('');}"
    "async function checkPW(){"
    "const pw=document.getElementById('pw-input').value;"
    "const h=await sha256(pw);"
    "if(h===MATERIALS_HASH){"
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

if old_js in html:
    html = html.replace(old_js, new_js, 1)
    print("Fixed: using direct password comparison")
else:
    print("Pattern not found - searching for pw gate...")
    idx = html.find('checkPW')
    print(repr(html[idx:idx+200]))

with open(DASHBOARD, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done!")
