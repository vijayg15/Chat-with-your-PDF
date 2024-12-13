# Chat-with-your-PDF
Here is an LLM-RAG application by using OpenAI where you can upload your own pdf file and can ask questions about it or can get response of your query.

## Steps to run the project

### Create a virtual environment pdfbot with python 3.9
```
conda create -n pdfbot python=3.9
```

### Activate the environment
```
conda activate pdfbot
```

### Install all the required packages and dependencies
```
pip install -r requirements.txt
```

### In [.env](.env) file set your API key.


### Now, run the application with 
```
    streamlit run app.py
```

### All the responses are recorded with it's query/question in [responses.json](responses.json) file.