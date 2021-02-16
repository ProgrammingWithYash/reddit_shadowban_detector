import requests
import os

acc_name = input("Enter Account Name >")

url = "https://www.reddit.com/user/" + acc_name

error = "Error"

# cls works on windows. You will need to change it for other operating systems. Eg. the clear console screen command for Linux is "clear"
system_clear_command = "cls"

os.system(system_clear_command)

print('Questioning Reddit about user - ' + acc_name)

while "Error" in error:
    # this gets all the html returned by the request
    html_content = requests.get(url).text

    if not "Something went wrong" in html_content:
        # the given sentence appears only if the user is banned or does not exist
        if "Sorry, nobody on Reddit goes by that name." in html_content:

            os.system(system_clear_command)
            print('If the account ' + acc_name +
                  ' exists, it is shadowbanned. Please don\'t kill me...')
            error = "Yes"
        else:
            os.system(system_clear_command)
            print('Everything looks fine for ' + acc_name +
                  '. Heartbeats back to normal...')
            error = "No"
    else:
        error = "Error"
        print("Reddit screwed up. Retrying ...")
