# python-genai-project-1
python-genai-project-1   
  
  
Note,   
latest working version: v0.2.0     

## ai-project (Gemini AI)    
-- **About the project**    
The 'python-genai-project-1' program provides a simple console interface that helps minimize the need to interact directly with the Google AI Studio web interface. Through the program's interface, various functions of the Gemini AI models can be accessed and utilized.     
   
Note:        
Accessing the Gemini AI API may require a 
Google Account, a Google AI Studio API key, 
and (optionally) a Gemini AI subscription.      
  
-- **Currently available features of the program:**    
-- -- you can choose a preset to use (from 'settings.json')                
-- -- you can write your prompts in the 'prompt.md' file        
-- -- you can observe Gemini AI responses in the 'response.md' file        
-- -- you can choose an AI model       
-- -- you can choose the AI model thinking_level        
-- -- you can test Gemini AI API connection (is_api_testing)        
-- -- you can send a SINGLE (one per session) prompt       
to Gemini AI             
-- -- you can send the prompt if you give permission      
or you can Abort the operation            
  
-- **Good to know about the program:**    
    
-- -- modifying or deleting preset_id 0 and it's settings is not recommended (in 'settings.json')              
-- -- you can manually overwrite    
model, thinking_level and selected_preset_id in 'settings.json'         
-- -- you can add new presets (with preset_id key and a number value) (in 'settings.json')      
**-- -- if you want to keep the contents of 'response.md'      
you HAVE TO SAVE IT to a different folder**        
-- -- Gemini AI API has     
rate limits, don't spam the AI.       
-- -- To see Gemini AI API rate limits for your account,             
see Google AI Studio website.      
-- -- Only single prompting is available in the program.      
(chat mode is not available).            
-- -- File import and file export     
is not available in the program.    
    
-- **Used program and tech versions**
- Google AI Studio         
- AI model (example): gemini-3.5-flash-lite       
- Python (python-3.14.3-amd64)    
- Python module 1: google-genai (2.28.0)     
- VS Code (VSCodeUserSetup-x64-1.58.2)     
  
-- **Example model to use (with the settings):**     
-- -- Tip: you can manually overwrite    
model, thinking_level and selected_preset_id in 'settings.json'    
```
gemini-3.5-flash-lite   
```
  
-- **Setup and Installation**    
 **project setup steps**      
   
-- -- install python    

-- -- install python module 1:      
(see 'Install python modules' section)    
(Name: google-genai     
Version: 2.28.0     
Summary: GenAI Python SDK          
)  

-- -- install VS Code

-- -- create ``` secrets/pass.txt ``` with 'GEMINI_API_KEY' value:   
(Put your real secret value in plain-text file here (only one value per file), no trailing newline needed.)      
(Get a free Gemini API key from Google AI Studio.)     
   
-- -- create a ``` prompt.md ``` in the project folder           
   
-- -- create an empty ``` response.md ``` in the project folder           
   
-- **Project run**    
  
-- -- Add 'GEMINI_API_KEY' to your ``` secrets/pass.txt ``` file          
-- -- open a new CMD terminal    
-- -- Start in: C:\Users\YourUsername\Desktop\ai-project         
-- -- start the program with ```python main.py```     
   
-- **Install python modules**      
   
-- -- open CMD     
-- -- you can use the following commands:         
  
-- -- pip install google-genai          
-- -- pip list         
-- -- pip show google-genai                               
-- -- (pip uninstall google-genai)          
     
-- **Settings made, setup**      
**Example 'settings.json' file:**   
   
```
{
    "settings": [
        {
            "selected_preset_id": "1"
        }
    ],
    "presets": [
        {
            "preset_id": "0",
            "model": "gemini-3.5-flash-lite",
            "contents": "Why is the sky blue?"
        },
        {
            "preset_id": "1",
            "model": "gemini-3.5-flash-lite",
            "thinking_level": "medium"
        },
        {
            "preset_id": "2",
            "model": "gemini-3.5-flash-lite",
            "thinking_level": "high"
        },
        {
            "preset_id": "3",
            "model": "gemini-3.5-flash-lite"
        }
    ]
}
```
