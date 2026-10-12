from google import genai


class Program:

    def __init__(self):
        pass

    def user_interface(self):
        print("1 - ...")
        print("2 - .. ..")
        print("3 - exit")

        while True:

            user_input = input("Choose from the menu options: ")

            if(user_input == "1"):
                AskGenAI.ask_ai()
                pass

            elif(user_input == "2"):
                Settings.print_settings()
                pass

            elif(user_input == "3"):
                print("Exiting...")
                break 

            else:
                print("Not a valid menu option. Please try again!")
 

class Settings:

    def __init__(self):
        pass

    def change_settings():
        print("! ! !")
        pass

    def print_settings():
        print("!!")
        pass


class AskGenAI:

    def __init__(self):
        pass

    def ask_ai():

        print("!")
        pass

        file = open("secrets/pass.txt", "r")    # Open the file in read mode

        file_content = file.read()      # read the file_content
        #client = genai.Client(api_key=file_content)
        file.close()

        #response = client.models.generate_content(
        #     model="gemini-3.5-flash-lite",
        #     contents="Why is the sky blue?"
        #
        #)
        #print(response.text)


# Run the program
start_program = Program()
start_program.user_interface()
