from google import genai

file = open("secrets/pass.txt", "r")    # Open the file in read mode

#client = file.read()    # read the file_content
#print(client)

file_content = file.read()      # read the file_content
client = genai.Client(api_key=file_content)
file.close()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Why is the sky blue?"

)

print(response.text)
