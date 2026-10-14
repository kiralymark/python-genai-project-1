from google import genai


class Program:

    def __init__(self):
        pass

    def user_interface(self):
        is_program_running = True

        print("\nMain Menu")
        print("1 - Ask AI")
        print("2 - Settings")
        print("3 - Exit Program")

        while is_program_running:

            user_input = input("\nChoose from the menu options: ")

            # menu Ask AI
            if(user_input == "1"):
                AskGenAI.ask_ai()
                pass

            # menu Settings
            elif(user_input == "2"):

                while True:
                    selected_preset_id = "1"

                    is_api_testing = False

                    print("\nSettings Menu")
                    print("Currently selected preset_id: " + selected_preset_id + "\n")
                    print("Currently used settings:")
                    print("model=")
                    print("contents=")
                    print("thinking_level=")
                    print("")

                    print("1 - Select a preset_id")
                    print("2 - Test API connection " + str(is_api_testing))
                    print("3 - Exit")

                    user_input = input("\nChoose from the menu options: ")

                    if(user_input == "1"):
                        print("Select...")
                        break

                    elif(user_input == "2"):
                        print("test...")
                        break

                    elif(user_input == "3"):
                        print("\nMain Menu")
                        print("1 - Ask AI")
                        print("2 - Settings")
                        print("3 - Exit Program")
                        break

                    else:
                        print("Not a valid menu option. Please try again!")
                
                #Settings.print_settings()
                #pass

            elif(user_input == "3"):
                print("Exiting...")
                is_program_running = False 

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
