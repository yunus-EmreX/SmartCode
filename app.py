import io
import webbrowser
import tkinter as tk
from flask import Flask, render_template, request, send_file
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_API_KEY'  # OpenAI API anahtarını buraya girin

user_input = ""
output = ""

def start_server():
    app.run(debug=False)

def open_web_interface():
    webbrowser.open("http://localhost:5000")

def create_code_interface():
    root = tk.Tk()
    root.title("ChatGPT Yazılım Oluşturma Arayüzü")

    def get_response():
        global user_input, output
        user_input = user_input_entry.get()

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=100
        )

        output = response.choices[0].text.strip()

        with open('output.txt', 'w') as file:
            file.write(output)

        output_label.config(text=output, fg="#333333")

    def download_code():
        with open('output.txt', 'r') as file:
            code = file.read()

        output = io.BytesIO()
        output.write(code.encode('utf-8'))
        output.seek(0)

        return send_file(output, attachment_filename='code.txt', as_attachment=True)

    def open_github():
        webbrowser.open("https://github.com/yunus-EmreX/syntaxdejecter")

    user_input_label = tk.Label(root, text="Metin Girişi:", fg="#333333")
    user_input_label.pack()

    user_input_entry = tk.Entry(root, width=50)
    user_input_entry.pack()

    submit_button = tk.Button(root, text="Gönder", command=get_response, bg="#4caf50", fg="white")
    submit_button.pack()

    output_label = tk.Label(root, text="", fg="#666666")
    output_label.pack()

    download_button = tk.Button(root, text="Kodu İndir", command=download_code, bg="#4caf50", fg="white")
    download_button.pack()

    syntax_label = tk.Label(root, text="Kodunda syntax ve girinti hataları mı var?", fg="#999999", cursor="hand2")
    syntax_label.pack(side=tk.BOTTOM, anchor=tk.SE)
    syntax_label.bind("<Button-1>", lambda e: open_github())

    version_label = tk.Label(root, text="Sürüm 0.93.6", fg="#999999")
    version_label.pack(side=tk.BOTTOM, anchor=tk.SE)

    developer_label = tk.Label(root, text="Yapımcı Yunus Emre Yüksel", fg="#999999")
    developer_label.pack(side=tk.BOTTOM, anchor=tk.SE)

    root.mainloop()

if __name__ == '__main__':
    start_server()
    open_web_interface()
    create_code_interface()
