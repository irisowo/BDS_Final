# BDS Final projet group13
### Target
```
Create a language learning assistant
```

### Function
```
1. Vocabulary Practice
2. Grammar Checker
3. Cloze Test
4. Joke Generator
5. Conversation
```

### Envirnment
```bash
conda create -n learnbot python=3.11
conda activate learnbot
pip install -r requirements.txt
```
Note that before running our bot, you should put an `.env` file under this project with
```bash
OPENAI_API_KEY=$your_openai_key
```

### QuickStart
```bash
streamlit run homepage.py
```