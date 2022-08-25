# Function with outputs

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return
    new_fname = f_name.title()
    new_lname = l_name.title()
    return f"{new_fname} {new_lname}"
    
# output = format_name("CIpher",".SH")
# print(output)

print(format_name(input("What is your first name? "),input("What is your last name? ")))

