from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig, pipeline
import torch
import textwrap
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


class chat_model:
    def __init__(self):
        self.tokenizer = LlamaTokenizer.from_pretrained("samwit/koala-7b")
        self.base_model = LlamaForCausalLM.from_pretrained(
            "samwit/koala-7b",
            load_in_8bit=True,
            device_map='auto',
        )
        self.pipe = pipeline(
            "text-generation",
            model=self.base_model, 
            tokenizer=self.tokenizer, 
            max_length=512,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.15
        )
        self.local_llm = HuggingFacePipeline(pipeline=self.pipe)

    def start_conversation(self):
        self.conversation = ConversationChain(
            llm=self.local_llm, 
            verbose=True, 
            memory=ConversationBufferWindowMemory(k=4)
        )

    def converse(self, input):
        self.conversation.prompt.template = '''The following is a friendly conversation between a human and an AI called Dolly. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know. 

        Current conversation:
        {history}
        Human: {input}
        AI:'''

        self.conversation.predict(input=input)
        return self.conversation(input)