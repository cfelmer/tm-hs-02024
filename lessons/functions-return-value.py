my_len = len("Caylee")
print(type(my_len))

def add_numbers(a,b):
    result = a+b 
    return result #sends result out

add_numbers(1,2)

new_number = add_numbers(1,2)
print(new_number)


def make_dictionary(first, last , phone, zip):
    return {
        "first_name" :first,
        "last_name" :last,
        "phone_number" :phone,
        "zip_code" :zip
    } 
caylee_data make_dictionary("caylee", "elmer","000-000-0000","100")
print(caylee_data["zip_code"])