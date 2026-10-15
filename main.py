from google import genai
import json

class Program:
    selected_preset_id = 0           # 0

    def __init__(self):
        pass

    def user_interface(self):
        is_program_running = True

        str_main_menu = ("\nMain Menu\n"
        "1 - Ask AI\n"
        "2 - Settings\n"
        "3 - Exit Program")

        str_not_valid_menu = "Not a valid menu option. Please try again!"

        str_choose_menu_message = "\nChoose from the menu options: "

        print(str_main_menu)

        while is_program_running:

            user_input = input(str_choose_menu_message)

            # menu Ask AI
            if(user_input == "1"):
                AskGenAI.ask_ai()
                pass

            # menu Settings
            elif(user_input == "2"):
                is_settings_menu_active = True

                while is_settings_menu_active:
                    #Program.selected_preset_id = "1"

                    is_api_testing = False

                    print("\nSettings Menu")
                    print("Currently selected preset_id: " + str(Program.selected_preset_id) + "\n")
                    print("Currently used settings:")
                    print("model=")
                    print("contents=")
                    print("thinking_level=")
                    print("")

                    print("1 - Select a preset_id")
                    print("2 - Test API connection " + str(is_api_testing))
                    print("3 - Exit")

                    user_input = input(str_choose_menu_message)

                    if(user_input == "1"):
                        is_valid_json = Settings.validate_settings()

                        Settings.print_all_preset_id()

                        #if(is_valid_json):
                            #user_input = input("\nChoose a preset_id: ")
                            # TO DO list all available preset id
                            # TO DO select a preset id

                        #pass

                    elif(user_input == "2"):
                        print("test...")
                        
                    elif(user_input == "3"):
                        print(str_main_menu)
                        is_settings_menu_active = False

                    else:
                        print(str_not_valid_menu)
                
            elif(user_input == "3"):
                print("Exiting...")
                is_program_running = False 

            else:
                print(str_not_valid_menu)
 

class Settings:

    def __init__(self):
        pass

    def validate_settings():
        with open("settings.json", "r") as file:    # Open the file in read mode
            file_content = file.read()      # read the file_content

        #is_valid_json
        try:
            json.loads(file_content)
            print("is valid json: True")
            return True
        except Exception as e:
            print("is valid json: False")
            print(e)
            return False

    def change_settings():
        #change value in settings (selected_preset_id)
        print("! ! !")
        pass

    def print_all_preset_id():
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData
                #file_content = json.loads(file)     # to load a string

                #print(file_content)
                #print(file_content['presets'])
                #print(file_content['presets'][0])
                #print(file_content['presets'][0][0])

                #for id in file_content[0]:
                    #preset_id_array = id.
                    #print(id)

                #for i in range(0,11):
                    #print(i)
                    #print(file_content['presets'][i])

                #for (key, value) in file_content.items():
                    #print(str(key) + " " + str(value))

                #for (key, value) in file_content['presets'][0].items():
                    #print(str(key) + " " + str(value))

                presets_count = len(file_content['presets'][0])
                #print(presets_count)
                for i in range(presets_count):
                    for (key, value) in file_content['presets'][i].items():
                        if(key == "preset_id"):
                            print(str(key) + " " + str(value))

            except Exception as e:
                print(e)

    def print_settings():
        # (selected_preset_id)
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
