HELP = """
'help' - enter (help) coomand, if you need help
'hello' - enter (hello) coomand, for greeting
'add' - enter (add) coomand, a name and a phone through the space for save
'change' - enter (change) coomand, an existing name and a new phone for changes 
'phone' - enter (phone) coomand, the name whose contact you need
'show all' - enter (show all) coomand, if you need to view all the data
'exit' - enter (exit) coomand, if you need close the program
 """


def input_error(my_func):
    def wrapper(*args):
        try:
            return my_func(*args)           
        except IndexError:
            return "(Index) Enter the command correctly or enter command (help)"

        except ValueError:
            return "(Value) Enter the name and phone correctly or enter command (help)" 

        except KeyError:
            return "(Key) Enter the name correctly or enter command (help)"

        except TypeError:
            return "Incorrect data entry. Enter the command, name and other correctly or enter command (help)"
   
    return wrapper


@input_error
def helping(*args):

    return HELP 


@input_error
def greeting(*args):

    return "How can I help you?"


contact_phones = {"ann": "0965035661",
                  "dan": "0969273178"}


@input_error
def add_data(data):
    name, phone = data
    if not contact_phones.get(name):
        contact_phones[name] = phone

    return f"{name.title()}: {phone}"

@input_error
def change_phone(data):
    name, phone = data
    if contact_phones.get(name):
        contact_phones[name] = phone

    return f"{name.title()}: {phone}"


@input_error
def output_phone(*args):
    for name in contact_phones.keys():
        inf_phone = f"{contact_phones.get(name)}" 

    return inf_phone 


def command_parser(user_input):
    for k, v in COMMANDS.items():
        if user_input.startswith(v):
            new_user_input = user_input.replace(v, "").split()
            
            return k, new_user_input
       
  
def main():
    print(HELP)
    while True:
        user_in = input("Please enter a command >>> ") 
        command, data  = command_parser(user_in)
        result = command(data)
        print(result)

        if command == exit:
            break
        
if __name__ == "__main__":
    main() 
