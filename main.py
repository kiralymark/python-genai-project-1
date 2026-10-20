from google import genai
from google.genai import types
import json

class Program:
    selected_preset_id = 0
    is_api_testing = False

    def __init__(self):
        Program.read_from_file_selected_preset_id()
        Settings.read_preset_settings(Program.selected_preset_id)

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
            Settings.read_preset_settings(Program.selected_preset_id)

            user_input = input(str_choose_menu_message)

            # menu Ask AI
            if(user_input == "1"):
                # check if a certain preset setting is available
                is_model_available = False
                is_contents_available = False
                is_thinking_level_available = False

                if(not(len(Settings.model) == 0)):
                    is_model_available = True
                if(not(len(Settings.contents) == 0)):
                    is_contents_available = True
                if(not(len(Settings.thinking_level) == 0)):
                    is_thinking_level_available = True

                if(Program.is_api_testing):
                    AskGenAI.ask_ai()   # ask_ai, plus ask ai confirmation messages
                else:
                    if(is_model_available and is_contents_available and not(is_thinking_level_available)):       # API TEST MODE
                        print("Error: Please use a different preset or enable 'Test API connection'!")
                    elif(is_model_available and not(is_contents_available) and not(is_thinking_level_available)):
                        is_permitted = AskGenAI.ask_ai_confirmation_messages()
                        if(is_permitted):
                            AskGenAI.ask_ai_2()
                        else:
                            print("Aborted...")
                    elif(is_model_available and not(is_contents_available) and is_thinking_level_available):
                        is_permitted = AskGenAI.ask_ai_confirmation_messages()
                        if(is_permitted):
                            AskGenAI.ask_ai_3()
                        else:
                            print("Aborted...")
                    else:
                        print("Error: Incorrect number and or type of parameters!")

                print(str_main_menu)
                Program.read_from_file_selected_preset_id()

            # menu Settings
            elif(user_input == "2"):
                is_settings_menu_active = True

                while is_settings_menu_active:

                    print("\nSettings Menu")
                    print("Currently selected preset ID: " + str(Program.selected_preset_id) + "\n")
                    print("Currently used settings:")
                    if(not(len(Settings.model) == 0)):
                        print("model = " + "'" + Settings.model + "'")
                    if(not(len(Settings.contents) == 0)):
                        print("contents = " + "'" + Settings.contents + "'")
                    if(not(len(Settings.thinking_level) == 0)):
                        print("thinking_level = " + "'" + Settings.thinking_level + "'")

                    print("\n1 - Select a preset_id")
                    print("2 - Test API connection " + "(" + str(Program.is_api_testing) + ")")
                    print("3 - Exit")

                    user_input = input(str_choose_menu_message)

                    if(user_input == "1"):
                        is_valid_json = Settings.validate_settings()

                        if(is_valid_json):
                            # List all available preset id
                            Settings.print_all_preset_id()

                            # Select a preset id
                            user_input = input("\nChoose a preset_id: ")

                            if not(len(user_input) == 0):
                                Settings.change_settings(user_input)

                    elif(user_input == "2"):
                        Program.is_api_testing = not(Program.is_api_testing)
                        
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
                print("ERROR: " + str(e))

        for (key, value) in file_content['settings'][0].items():
            if(key == "selected_preset_id"):
                Program.selected_preset_id = value
    

class Settings:
    model = ""
    contents = ""
    thinking_level = ""

    def __init__(self):
        pass

    def validate_settings():
        with open("settings.json", "r") as file:    # Open the file in read mode
            file_content = file.read()      # read the file_content

        #is_valid_json
        try:
            json.loads(file_content)
            return True
        
        except Exception as e:
            print("ERROR: " + str(e))
            return False

    def change_settings(user_input):
        # Change value in settings (selected_preset_id)

        list_available_id = []

        # (READ FILE)
        # Confirm if 'selected preset id' is valid (from user_input) 
                
        # iterate through json, get all available ID
        # if ID exists, select it,
        # else throw error message

        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData
                presets_count = len(file_content['presets'])
                for i in range(presets_count):
                    for (key, value) in file_content['presets'][i].items():
                        if(key == "preset_id"):
                            list_available_id.append(str(value))

            except Exception as e:
                print("ERROR: " + str(e))

        is_searching_value = True
        for id in list_available_id:
            if is_searching_value:
                if(user_input == id):
                    is_searching_value = False

        if is_searching_value == True:
            print("Preset ID " + user_input + " cannot be found. Please try again!")
        else:
            # Save changes to JSON file (write to file)
            Settings.write_to_file_settings(user_input)

    def write_to_file_settings(user_input):
        # (Save changes to JSON file (write to file))
        
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData

            except Exception as e:
                print("ERROR: " + str(e))

        with open("settings.json", "w") as file:
            try:
                file_content.update({"settings": [{"selected_preset_id" : str(user_input)}]})
                file.write(json.dumps(file_content, indent=4))

            except Exception as e:
                print("ERROR: " + str(e))

    def print_all_preset_id():
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData
                presets_count = len(file_content['presets'])
                for i in range(presets_count):
                    for (key, value) in file_content['presets'][i].items():
                        if(key == "preset_id"):
                            print(str(key) + " " + str(value))

            except Exception as e:
                print("ERROR: " + str(e))

    def read_preset_settings(selected_preset_id):
        # (selected_preset_id)
        # Read from file and then store the settings

        # Read preset settings that belong to a preset_id
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData

                presets_count = len(file_content['presets'])
                is_searching_settings = False

                dict_preset_settings = {}
                for i in range(presets_count):
                    for (key, value) in file_content['presets'][i].items():
                        if(key == "preset_id" and value == selected_preset_id):
                            is_searching_settings = True
                        elif(key == "preset_id" and (not value == selected_preset_id)):
                            is_searching_settings = False
                        if(is_searching_settings):
                            if(key == "model"):
                                dict_preset_settings[key] = value
                            if(key == "contents"):
                                dict_preset_settings[key] = value
                            if(key == "thinking_level"):   
                                dict_preset_settings[key] = value 

                if(not(len(dict_preset_settings) == 0)):
                    Settings.store_preset_settings(dict_preset_settings)

            except Exception as e:
                print("ERROR: " + str(e))      

    def store_preset_settings(dict_preset_settings):        # (set_preset_settings)
        # Store preset settings
        
        # Key-value pairs store in Settings class
        # Overwrite stored values if needed
        # Add certain key value pair or delete (set to "" string)
        is_model_available = False
        is_contents_available = False
        is_thinking_level_available = False
        for (key, value) in dict_preset_settings.items():
            if(key == "model"):
                Settings.model = value
                is_model_available = True
            if(key == "contents"):
                Settings.contents = value
                is_contents_available = True
            if(key == "thinking_level"):
                Settings.thinking_level = value 
                is_thinking_level_available = True

        # Decide if a certain setting is available (TRUE/FALSE)
        if(not(is_model_available)):
            Settings.model = ""
        if(not(is_contents_available)):
            Settings.contents = ""
        if(not(is_thinking_level_available)):
            Settings.thinking_level = ""


class AskGenAI:

    def __init__(self):
        pass

    def ask_ai_confirmation_messages(model = "", content = ""):
        # - let user decide if settings acceptable
        # - print settings
        # - print out current prompt

        print("\nCurrent settings: ")

        if(Program.is_api_testing):         # API TEST MODE
            print("API TESTING")
            print("model = " + "'" + str(model) + "'")
            print("contents = " + "'" + str(content) + "'")
        else:                                                   # ask_ai mode
            print("preset_id = " + "'" + str(Program.selected_preset_id) + "'")
            if(not(len(Settings.model) == 0)):
                print("model = " + "'" + str(Settings.model) + "'")
            if(not(len(Settings.thinking_level) == 0)):
                print("thinking_level = " + "'" + str(Settings.thinking_level) + "'")

            print("contents = ")
            print("\"\"\"\n" + str(AskGenAI.read_from_file_prompt()) + "\n\"\"\"")

        print("\nDo you want to send the prompt with these settings?")
        user_input = input("(y/n): ")

        if(user_input.lower() == "y" or user_input.lower() == "yes"):
            return True
        else:
            return False

    # ask_ai_1()    # Zero parameters, default test method (in production version do not modify)
    def ask_ai():
        # - ask ai confirmation messages
        # - ask ai

        file = open("secrets/pass.txt", "r")    # Open the file in read mode

        file_content = file.read()      # read the file_content
        client = genai.Client(api_key=file_content)
        file.close()

        # Load the preset settings for ' preset_id 0 '
        # read from file (settings json)

        dict_preset_settings = {}
        with open("settings.json", "r") as file:    # Open the file in read mode
            try:
                file_content = json.load(file)      # to load a JSON object ; jsonData
                presets_count = len(file_content['presets'])

                is_searching_value = True
                for i in range(presets_count):
                    if(is_searching_value):
                        for (key, value) in file_content['presets'][i].items():
                            if(key == "preset_id" and value == "0"):
                                is_searching_value = False
                            if(key == "model"):
                                dict_preset_settings[key] = value
                            if(key == "contents"):
                                dict_preset_settings[key] = value

                if(len(dict_preset_settings) == 0):
                    print("Error: " + "Settings for Preset ID 0 cannot be found!")

            except Exception as e:
                print("ERROR: " + str(e))

        model = str(dict_preset_settings["model"])
        content = str(dict_preset_settings["contents"])

        # ask ai confirmation messages
        is_permitted = AskGenAI.ask_ai_confirmation_messages(model, content)

        if(is_permitted):
            print("\nresponse = ")
            print("\"\"\"")
            response = client.models.generate_content(
                 model=model,
                 contents=content
            )
            print(response.text)
            print("\"\"\"")

            AskGenAI.write_to_file_response(response.text)
        else:
            print("Aborted...")

    # ask_ai_2()    # only model is available
    def ask_ai_2():

        file = open("secrets/pass.txt", "r")    # Open the file in read mode

        file_content = file.read()      # read the file_content
        client = genai.Client(api_key=file_content)
        file.close()

        file_prompt_content = str(AskGenAI.read_from_file_prompt())
        
        response = client.models.generate_content(
             model=Settings.model,
             contents=file_prompt_content
        )
        print("\nresponse = ")
        print("\"\"\"")
        print(response.text)
        print("\"\"\"")

        AskGenAI.write_to_file_response(response.text)

    # ask_ai_3()    # model and thinking_level is available
    def ask_ai_3():

        file = open("secrets/pass.txt", "r")    # Open the file in read mode

        file_content = file.read()      # read the file_content
        client = genai.Client(api_key=file_content)
        file.close()

        file_prompt_content = str(AskGenAI.read_from_file_prompt())

        # is_thinking_level_valid = False
        # if(str(Settings.thinking_level).upper() == "MINIMAL"):
        #     thinking_level_content = genai.types.ThinkingLevel.MINIMAL
        #     is_thinking_level_valid = True 
        # elif(str(Settings.thinking_level).upper() == "LOW"):
        #     thinking_level_content = genai.types.ThinkingLevel.LOW
        #     is_thinking_level_valid = True 
        # elif(str(Settings.thinking_level).upper() == "MEDIUM"):
        #     thinking_level_content = genai.types.ThinkingLevel.MEDIUM
        #     is_thinking_level_valid = True 
        # elif(str(Settings.thinking_level).upper() == "HIGH"):
        #     thinking_level_content = genai.types.ThinkingLevel.HIGH
        #     is_thinking_level_valid = True 
        # else:
        #     print("Error: " + "Setting for 'ThinkingLevel' cannot be found!")
        #     return None


        response = client.models.generate_content(
            model=Settings.model,
            contents=file_prompt_content,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_level=Settings.thinking_level
                )
            )
        )
        
        # error 03
        #
        # if(is_thinking_level_valid):
        #     response = client.models.generate_content(
        #         model=Settings.model,
        #         contents=file_prompt_content,
        #         config=genai.types.GenerateContentConfig(
        #             thinking_config=genai.types.ThinkingConfig(
        #                 thinking_level=genai.ThinkingLevel.MEDIUM
        #             )
        #         )
        #     )

        # error 02
        #
        # response = client.models.generate_content(
        #     model=Settings.model,
        #     contents=file_prompt_content,
        #     generation_config={
        #         "thinking_level": Settings.thinking_level
        #     }
        # )

        # error 01
        #
        # response = client.models.generate_content(
        #     model=Settings.model,
        #     contents=file_prompt_content,
        #     config=types.GenerateContentConfig(
        #         thinking_config=types.ThinkingConfig(
        #             thinking_level=Settings.thinking_level
        #         )
        #     )
        # )



        print("\nresponse = ")
        print("\"\"\"")
        print(response.text)
        print("\"\"\"")

        AskGenAI.write_to_file_response(response.text)

    def read_from_file_prompt():

        with open("prompt.md", "r") as file:
            try:
                file_content = file.read()

            except Exception as e:
                print("ERROR: " + str(e))

        return file_content

    def write_to_file_response(response_text):

        with open("response.md", "w") as file:
            try:
                file.write(response_text)

            except Exception as e:
                print("ERROR: " + str(e))


# Run the program
start_program = Program()
start_program.user_interface()
