import json

from csv import DictReader


def library():
    """library creation function"""
    with open('books.csv', 'r') as b:
        # reading file with books
        result = []
        books = DictReader(b)

        with open('users.json', 'r') as u:
            # reading file with users
            users = json.load(u)

            for user in users:
                # adding books item to the end of the list
                result.append(
                    {
                        'name': user['name'],
                        'gender': user['gender'],
                        'address': user['address'],
                        'age': user['age'],
                        'books': []
                    }
                )

            user_number = len(result)
            i = 0
            print(result)
            for book in books:
                # distribution of books among users
                user = result[i % user_number]
                user['books'].append(
                    {
                        'title': book['Title'],
                        'author': book['Author'],
                        'pages': book['Pages'],
                        'genre': book['Genre'],
                    }
                )
                i += 1

            with open('result.json', 'w') as r:
                # writing the result to the final file
                res = json.dumps(result, indent=4)
                r.write(res)


library()
