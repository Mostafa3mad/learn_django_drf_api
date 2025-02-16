import requests
json={'student_id': 2,
      'name': 'emad salah2',
      'branch': 'cs'
      }
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'X-CSRFTOKEN': 'PtKSuW9onxtY9fqV4BbSjcHFuLnPq8gw2MeeYaxgcY4tkcsxvlPZr61bs2DS2lXd',
    'Referer': 'http://127.0.0.1:8000/api/v1/students/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Accept': 'text/html; q=1.0, */*',
    'X-KL-saas-Ajax-Request': 'Ajax_Request',
    'Content-Type': 'application/json',
}

responce = requests.put("http://127.0.0.1:8000/api/v1/students/2/",json=json)
print(responce.status_code)
