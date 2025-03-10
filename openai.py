from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'http://127.0.0.1:5000/generate-doc'

def generate_documentation(code_snippet):
    prompt = f"Generate detailed documentation for the following Python code:\n\n{code_snippet}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/generate-doc', methods=['POST'])
def generate_doc():
    data = request.get_json()
    code_snippet = data.get("code", "")
    if not code_snippet:
        return jsonify({"error": "No code snippet provided"}), 400
    documentation = generate_documentation(code_snippet)
    return jsonify({"documentation": documentation})

if __name__ == '__main__':
    app.run(debug=True)
