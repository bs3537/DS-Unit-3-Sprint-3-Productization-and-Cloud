#pipenv install basilica, python-dotenv
import os
from dotenv import load_dotenv
import basilica
load_dotenv()
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
with basilica.Connection(BASILICA_API_KEY) as c:
    embeddings = list(c.embed_sentences(sentences))
print(embeddings)

#File is working fine as of 2/14/2020, 9.15 PM.