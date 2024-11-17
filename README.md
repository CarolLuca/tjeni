This is the frontend of the application for AIRo team at digital justice hackathon

You can find the backend on the vm

To run:

1. Make and activate venv

```py
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```py
pip install -r requirements.txt
```

3. Run frontend

```sh
chmod 777 run.sh
./run.sh
```


## Backend

- go on the /workspace folder

```py
cd Similarity
```

```py
# activate environment (this venv already exists, DO NOT recreate it)
source venv/bin/activate
cd ..
```

- do NOT install any other requirements.txt files (they are already installed in the venv)


```sh
# run the uvicorn command in the run_app.sh
uvicorn main:asgi_app --host 0.0.0.0 --port 8080
```

- now the server is running and the frontend can connect to it :)


# Backend info

- workspace/cont - containment score and position embeddings
- workspace/Similarity - utils and pipelines
- workspace/Similarity/utils, workspace/ner - pipelines: 
    -   GermanNer, 
    -   EnglNer
    -   Translation, 
    -   ZeroShot topic classification
    -   File cleaners & normalizers
- workspace/Similarity/faiss_*.py - faiss db
- workspace/Similarity/vectordb.py - chroma db 
- workspace/Similarity/test_*.py - unittests for pipelines
