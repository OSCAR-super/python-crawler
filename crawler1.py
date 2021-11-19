import time
from urllib.request import urlopen
from urllib.request import Request
import json
import pymysql
import numpy as np
def get_results(search, headers, page, stars):
    url = 'https://api.github.com/search/repositories?q={search}%20stars:<={stars}&page={num}&per_page=100&sort=stars' \
          '&order=desc'.format(search=search, num=page, stars=stars)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())
    return result


if __name__ == '__main__':
    # Specify JavaScript Repository
    search = 'language:javascript'

    # Modify the GitHub token value
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'token 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',
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }

    count = 1
    # The highest value of JavaScript repository STAR is 321701, repository is freeCodeCamp.
    stars = 421701
    conn = pymysql.connect(host="127.0.0.1", user="root", password='123456', db="mysql")
    cursor = conn.cursor()
    cursor.execute("select * from python_c")
    fetch=cursor.fetchall()
    for i in range(0, 2):
        repos_list = []
        stars_list = []
        for page in range(1, 11):
            results = get_results(search, headers, page, stars)
            for item in results['items']:
                repos_list.append([count, item["name"], item["clone_url"]])
                stars_list.append(item["stargazers_count"])
                count += 1
            print(len(repos_list))
        stars = stars_list[-1]
        print(stars)
        x=np.zeros(len(repos_list))
        for i in range(0,len(repos_list)):
            for j in range(i+1, len(repos_list)):
                if repos_list[j][2]==repos_list[i][2] and repos_list[j][1]!=repos_list[i][1]:
                    repos_list[j][1] = repos_list[i][1]
        for i in range(len(repos_list)):
            for j in range(0, len(fetch)):
                if fetch[j][2]==repos_list[i][2]:
                    x[i]+=1
            if x[i]==0:
                sql = "insert into python_c (id,proname, web) VALUES ("+"null,'"+repos_list[i][1] +"','"+repos_list[i][2] +"' )"
                print(sql)
                cursor.execute(sql)
                conn.commit()
        # For authenticated requests, 30 requests per minute
        # For unauthenticated requests, the rate limit allows you to make up to 10 requests per minute.
        time.sleep(60)
    cursor.close()
    conn.close()