def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Name: {name} Lastname: {lastname} Year of birth: {year_of_birth}'
                 f'City: {city} Email: {email} Phone: {phone}')


personal_data(
    name=input('Name: '),
    lastname=input('lastname: '),
    year_of_birth=input('Year of birth: '),
    city=input('City: '),
    email=input('email: '),
    phone=input('phone: '),
)