# Recommendation System

Recommended to be used with PyCharm IDE.

Run below in the terminal to install the requirements and start the service:

```bash
# Install the requirements:
pip install -r requirements.txt

# Start the service:
uvicorn app:app --reload
```

Now you can load http://localhost:8000/docs in your browser ... but there won't be much to see until you've inserted
some data.

You can test with,

    existing_profile = "64315d86362c27c707fe155c"

    new_profile = "64315d86362c27c707fe152z"

    sentiment = "The restaurant provided updates on the status of our order, which was very helpful."


Repleace sentiment prediction part
Model
Requarement

pip install motor==3.1.2 pandas==2.0.0 fastapi==0.95.1 pydantic==1.10.7 python-dotenv==1.0.0 numpy scipy==1.10.1 scikit-learn nltk gensim keras tensorflow-cpu==2.8.0 textblob==0.17.1

pip install uvicorn mangum protobuf==3.19