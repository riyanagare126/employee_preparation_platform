import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.app import create_app

app = create_app()
client = app.test_client()

def test_module(slug, mod, role):
    res = client.get(f'/api/companies/{slug}/modules/{mod}?role={role}')
    data = res.get_json()
    qs = data.get('questions', []) or data.get('problems', [])
    return [q.get('question') or q.get('description') or q.get('title') for q in qs[:3]]

print('--- APTITUDE (Java Developer) ---')
g_apt = test_module('google', 'aptitude', 'Java Developer')
t_apt = test_module('tcs', 'aptitude', 'Java Developer')
print('Google Aptitude Sample:', g_apt[0])
print('TCS Aptitude Sample:', t_apt[0])
assert g_apt[0] != t_apt[0], 'Aptitude questions should not match!'

print('\n--- CODING (Python Developer) ---')
amz_code = test_module('amazon', 'coding', 'Python Developer')
infy_code = test_module('infosys', 'coding', 'Python Developer')
print('Amazon Coding Sample:', amz_code[0][:80])
print('Infosys Coding Sample:', infy_code[0][:80])
assert amz_code[0] != infy_code[0], 'Coding questions should not match!'

print('\n--- TECHNICAL (Java Developer) ---')
msft_tech = test_module('microsoft', 'technical', 'Java Developer')
acc_tech = test_module('accenture', 'technical', 'Java Developer')
print('Microsoft Technical Sample:', msft_tech[0])
print('Accenture Technical Sample:', acc_tech[0])
assert msft_tech[0] != acc_tech[0], 'Technical questions should not match!'

print('\n--- HR (Data Analyst) ---')
rh_hr = test_module('redhat', 'hr', 'Data Analyst')
del_hr = test_module('deloitte', 'hr', 'Data Analyst')
print('Red Hat HR Sample:', rh_hr[0])
print('Deloitte HR Sample:', del_hr[0])
assert rh_hr[0] != del_hr[0], 'HR questions should not match!'

print('\n--- AI INTERVIEW (Python Developer) ---')
ibm_ai = test_module('ibm', 'interview', 'Python Developer')
cap_ai = test_module('capgemini', 'interview', 'Python Developer')
print('IBM AI Interview Sample:', ibm_ai[0])
print('Capgemini AI Interview Sample:', cap_ai[0])
assert ibm_ai[0] != cap_ai[0], 'AI Interview questions should not match!'

print('\n=============================================')
print('SUCCESS: ALL LIVE ENDPOINTS RETURN DISTINCT QUESTIONS!')
print('=============================================')
