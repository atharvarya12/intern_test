import textwrap
import google.generativeai as genai  
from IPython.display import Markdown



def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


MODEL_NAME = 'gemini-pro' 

generation_config = {
        "temperature": 0.9,
        "top_k": 1,
        "top_p": 1,
        "max_output_tokens": 1000,
    }

async def load_story(user_input):
    genai.GenerationConfig('AIzaSyDGVJeOyL_4QuyTpesToDeirGhc24DbDug')
    model = genai.GenerativeModel(MODEL_NAME)
    
  

    chat = model.start_chat()

    result = await chat.send_message(user_input,
                                     generation_config=generation_config,
                                     )  
    return result.response.content
 

def answer_questions(story_text, question):
    genai.GenerationConfig('AIzaSyDGVJeOyL_4QuyTpesToDeirGhc24DbDug')
    model = genai.GenerativeModel(MODEL_NAME)

    chat = model.start_chat()
    request = chat.send_message(
    genration_config=generation_config,
    SafetySettingOptions = None,
    bool = False,
    )
    
    
async def main():
    story_text = load_story()

    while True:
        question = input("Ask a question about the story: ")
        if question.lower() == 'exit':
            break

        answer = answer_questions(story_text, question)
        print("Answer:", answer)

if __name__ == "__main__":
    import asyncio
    asyncio.run.main()
