import gradio as gr


title = "My first Demo with Hugging Face"
description = "This is a demo as a example"



gr.Interface.load("models/oliverguhr/german-sentiment-bert").launch(share=True)