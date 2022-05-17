file_path = 'galerie.txt'
ex_file_path = 'galerie_przyklad.txt'
wynik41 = 'wynik4_1.txt'
wynik42a = 'wynik4_2a.txt'
wynik42b = 'wynik4_2b.txt'
wynik43 = 'wynik4_3.txt'

def zadanie():
   countries = dict()
   cities = dict()
   biggest_galery = {
      'name': '',
      'size': 0,
   }
   smallest_galery = {
      'name': '',
      'size': 0
   }
   galery_with_least_unique_stores = {
      'name': '',
      'amount': 0
   }
   galery_with_most_unique_stores = {
      'name': '',
      'amount': 0
   }
   with open(file_path, 'r') as file:
      for line in file:
         country, city, *sizes = line.split()
         store_count = 0
         galery_size = 0
         unique_locals = set()
         if country not in countries.keys():
             countries[country] = 1
         else:
            countries[country] += 1
         if city not in cities.keys():
            cities[city] = {
               'galery_size': galery_size,
               'store_count': store_count
            }
         index = 1
         while index <= 140:
            size = int(sizes[index]) * int(sizes[index - 1])
            if size != 0:
               store_count += 1
            galery_size += size
            if size > 0 and size not in unique_locals:
               unique_locals.add(size)
            index += 2
         cities[city] = {
            'galery_size': galery_size,
            'store_count': store_count,
            'unique_locals': len(unique_locals)
         }
   for city_galery in cities:
      galery_size = cities[city_galery]['galery_size']
      unique_locals = cities[city_galery]['unique_locals']
      if galery_size > biggest_galery['size']:
         biggest_galery['name'] = city_galery
         biggest_galery['size'] = galery_size
      if smallest_galery['size'] == 0 or galery_size < smallest_galery['size']:
         smallest_galery['name'] = city_galery
         smallest_galery['size'] = galery_size
      if unique_locals > galery_with_most_unique_stores["amount"]:
         galery_with_most_unique_stores['name'] = city_galery
         galery_with_most_unique_stores['amount'] = unique_locals
      if galery_with_least_unique_stores['amount'] == 0 or unique_locals < galery_with_least_unique_stores['amount']:
         galery_with_least_unique_stores['name'] = city_galery
         galery_with_least_unique_stores['amount'] = unique_locals

   # zapisywanie odpowiedzi
   with open(wynik41, 'w') as file_ans:
      for country in countries:
         answer = f'{country} {countries[country]}\n'
         file_ans.write(answer)
   with open(wynik42a, 'w') as file_ans:
      for city in cities:
         answer = f'{city} {cities[city]["galery_size"]} {cities[city]["store_count"]}\n'
         file_ans.write(answer)
   with open(wynik42b, 'w') as file_ans:
      answer = f'{biggest_galery["name"]} {biggest_galery["size"]}\n{smallest_galery["name"]} {smallest_galery["size"]}'
      file_ans.write(answer)
   with open(wynik43, 'w') as file_ans:
      answer = f'{galery_with_most_unique_stores["name"]} {galery_with_most_unique_stores["amount"]}\n{galery_with_least_unique_stores["name"]} {galery_with_least_unique_stores["amount"]}'
      file_ans.write(answer)



zadanie()
