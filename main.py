from google import genai

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


# temporary code 
#file_content = file.read()      # read the file_content
# client = genai.Client(api_key=file_content)
#file.close()

#model = file.read()
#prompt = file.read()
#include_thoughts = file.read() # values: True / False
#thinking_level = file.read()   # values: "low" , "medium" , "high"

# response = client.models.generate_content(
#     model=model,
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         max_output_tokens=5000,
#         thinking_config=types.ThinkingConfig(
#             include_thoughts=False,
#             thinking_level="high"
#         )
#     )
# )
#print(response.text)

##    'max_output_tokens': 4096,

##        thinking_config=types.ThinkingConfig(
##            thinking_budget=0                         # thinking_budget=1024
##        )


# Alternative code (to set gemini ai thinking level)     
# tools = [
#     {
#         'type': 'code_execution',
#     },
#     {
#         'type': 'google_search',
#     },
# ]

# generation_config = {
#     'max_output_tokens': 4096,
#     'thinking_level': 'high',
# }

# interaction = client.interactions.create(
#     model='models/gemini-3.8-flash',
#     input="""INSERT_INPUT_HERE""",
#     tools=tools,
#     generation_config=generation_config,
# )

# print(interaction.steps[-1])


# to use chat mode
#chat = client.chats.create(model="gemini-3.5-flash-lite")

# to upload (/import) files to Gemini AI
#uploaded_file = client.files.upload(file="image.jpg")
#uploaded_file = client.files.upload(file="audio.mp3")
#response = client.models.generate_content(
#     model="gemini-3.5-flash-lite",
#     contents=["Describe this image for me", uploaded_file]
#
#)
#response = client.models.generate_content(
#     model="gemini-3.5-flash-lite",
#     contents=["Transcribe this audio for me", uploaded_file]
#
#)
# for pdf files ...
#response = client.models.generate_content(
#     model="gemini-3.5-flash-lite",
#     contents=["Extract the dates and the prices from the file.", uploaded_file]
#
#)
#print(response.text)


# Write response to file     

# file = open("prompt.md", "r")    # Open the file in read mode

# file_content = file.read()      # read the file_content
# file.close()

# response = file_content

# print(response)

# with open("response.md", "w", encoding="utf-8") as file_output:
#     file_output.write(response)
