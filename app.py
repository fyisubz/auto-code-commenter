from openai import OpenAI
import gradio as gr

client = OpenAI(api_key="API_KEY",  base_url="https://openrouter.ai/api/v1")
def auto_commenter(code):
    try:
        prompt = f"Add meaningful comments to the following code:\n\n{code}"
        response = client.chat.completions.create(
            model="x-ai/grok-4-fast:free",
            messages=[{"role": "user","content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(
    fn=auto_commenter,
    inputs=gr.Textbox(lines=15, placeholder="Paste your code here..."),
    outputs=gr.Textbox(lines=15),
    title="Auto Code Commenter",
    description="Enter your code, and the AI will add meaningful comments to it."

)

iface.launch()
