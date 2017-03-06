data = '''
{
  "note":"This file contains the actual data for your assignment",
  "comments":[
    {
      "name":"Warrick",
      "count":98
    },
    {
      "name":"Angali",
      "count":97
    },
    {
      "name":"Reece",
      "count":96
    },
    {
      "name":"Babatunmise",
      "count":92
    },
    {
      "name":"Krishan",
      "count":91
    },
    {
      "name":"Lillyann",
      "count":88
    },
    {
      "name":"Apryl",
      "count":86
    },
    {
      "name":"Hadiyah",
      "count":86
    },
    {
      "name":"Connie",
      "count":81
    },
    {
      "name":"Cadence",
      "count":80
    },
    {
      "name":"Nevan",
      "count":80
    },
    {
      "name":"Brook",
      "count":78
    },
    {
      "name":"Zohair",
      "count":75
    },
    {
      "name":"Kiera",
      "count":69
    },
    {
      "name":"Noelani",
      "count":68
    },
    {
      "name":"Paul",
      "count":63
    },
    {
      "name":"Layne",
      "count":62
    },
    {
      "name":"Sasha",
      "count":60
    },
    {
      "name":"Danish",
      "count":59
    },
    {
      "name":"Conlyn",
      "count":58
    },
    {
      "name":"Dharci",
      "count":55
    },
    {
      "name":"Matteo",
      "count":54
    },
    {
      "name":"Kenton",
      "count":53
    },
    {
      "name":"Morvyn",
      "count":53
    },
    {
      "name":"Keira",
      "count":51
    },
    {
      "name":"Tian",
      "count":51
    },
    {
      "name":"Leonah",
      "count":47
    },
    {
      "name":"Daniels",
      "count":46
    },
    {
      "name":"Lisandro",
      "count":46
    },
    {
      "name":"Regina",
      "count":41
    },
    {
      "name":"Shanyse",
      "count":38
    },
    {
      "name":"Karice",
      "count":33
    },
    {
      "name":"Maliha",
      "count":32
    },
    {
      "name":"Bianca",
      "count":31
    },
    {
      "name":"Kacie",
      "count":31
    },
    {
      "name":"Drew",
      "count":29
    },
    {
      "name":"Kiya",
      "count":25
    },
    {
      "name":"Eleonora",
      "count":25
    },
    {
      "name":"Kynan",
      "count":24
    },
    {
      "name":"Micheal",
      "count":21
    },
    {
      "name":"Nuwaira",
      "count":21
    },
    {
      "name":"Jodi",
      "count":19
    },
    {
      "name":"Shanzay",
      "count":18
    },
    {
      "name":"Areej",
      "count":18
    },
    {
      "name":"Rayna",
      "count":17
    },
    {
      "name":"Scott",
      "count":11
    },
    {
      "name":"Ciarian",
      "count":10
    },
    {
      "name":"Hanania",
      "count":9
    },
    {
      "name":"Hena",
      "count":2
    },
    {
      "name":"Abigail",
      "count":1
    }
  ]
}
'''


import json
info = json.loads(data)

count = -1
sum = 0
count_not_finished = True

while count_not_finished:
    for item in info:
        if item == "comments":
            count += 1
        if count > 100:
            count_not_finished = False
            break
        item = str(item)
        try:
            value = info[item][count]["count"]
        except:
            continue
        sum += value
        
print("sum is: ", sum)
    