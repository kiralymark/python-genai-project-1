from google import genai
import json

class Program:
    selected_preset_id = 0           # 0

    def __init__(self):
        #selected_preset_id = 
        Program.read_from_file_selected_preset_id()

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
            Program.read_from_file_selected_preset_id()

            user_input = input(str_choose_menu_message)

            # menu Ask AI
            if(user_input == "1"):
                AskGenAI.ask_ai()
                Program.read_from_file_selected_preset_id()
                pass

            # menu Settings
            elif(user_input == "2"):
                is_settings_menu_active = True

                while is_settings_menu_active:
                    #Program.selected_preset_id = "1"

                    is_api_testing = False

                    print("\nSettings Menu")
                    print("Currently selected preset ID: " + str(Program.selected_preset_id) + "\n")
                    print("Currently used settings:")
                    print("model=")
                    print("contents=")
                    print("thinking_level=")
                    print("")

                    print("1 - Select a preset_id")
                    print("2 - Test API connection " + "(" + str(is_api_testing) + ")")
                    print("3 - Exit")

                    user_input = input(str_choose_menu_message)

                    if(user_input == "1"):
                        is_valid_json = Settings.validate_settings()

                        if(is_valid_json):
                            # TO DO list all available preset id
                            Settings.print_all_preset_id()

                            # TO DO select a preset id
                            user_input = input("\nChoose a preset_id: ")

                            if not(len(user_input) == 0):
                                #print("*")
                                Settings.change_settings(user_input)

                    elif(user_input == "2"):
                        print("test...")
                        
                    elif(user_input == "3"):
                        print(str_main_menu)
                        is_settings_menu_active = False

                    else:
                        print(str_not_valid_menu)

                    Program.read_from_file_selected_preset_id()

            elif(user_input == "3"):
                print("Exiting...")
                is_program_running = False 

            else:
                print(str_not_valid_menu)
 
    def read_from_file_selected_preset_id():
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData

            except Exception as e:
                print(e)

        #print(file_content['settings'][0])
        #for (key, value) in file_content['settings'][0].items():
        #    if(key == "selected_preset_id"):
        #        print(value)

        for (key, value) in file_content['settings'][0].items():
            if(key == "selected_preset_id"):
                Program.selected_preset_id = value

        #Program.selected_preset_id = print(file_content['presets'][0])
    

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

    def change_settings(user_input):
        #change value in settings (selected_preset_id)

        list_available_id = []

        # (READ FILE)
        # todo: confirm if 'selected preset id' is valid (from user_input) 
                
        # iterate through json, get all available ID
        # if ID exists, select it,
        # else throw error message

        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData
                presets_count = len(file_content['presets'][0])
                for i in range(presets_count):
                    for (key, value) in file_content['presets'][i].items():
                        if(key == "preset_id"):
                            list_available_id.append(str(value))

            except Exception as e:
                print(e)

        is_searching_value = True
        for id in list_available_id:
            if is_searching_value:
                if(user_input == id):
                    #print("test...")
                    is_searching_value = False

        if is_searching_value == True:
            print("Preset ID " + user_input + " cannot be found. Please try again!")
        else:
            # todo: save changes to JSON file (write to file)
            Settings.write_to_file_settings(user_input)

        print("! ! !")

    def write_to_file_settings(user_input):
        # (save changes to JSON file (write to file))
        
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData

            except Exception as e:
                print(e)

        print(file_content['settings'][0])
            #if(key == "selected_preset_id"):
            #    print()

        #for (key, value) in file_content['settings'][0].items():
        #    if(key == "selected_preset_id"):
        #        print(value)

        with open("settings.json", "w") as file:
            try:
                #file_content.update({"selected_preset_id" : str(user_input)})
                #file_content_modified = json.dumps(file_content)
                #print(file_content_modified)

                file_content.update({"settings": [{"selected_preset_id" : str(user_input)}]})
                file.write(json.dumps(file_content, indent=4))

            except Exception as e:
                print(e)

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
        # read from file
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
