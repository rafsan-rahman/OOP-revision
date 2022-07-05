from transformers import AutoTokenizer
from transformers import AutoModel

#input data
sentences = ["আমি পারি না আর পারি না","খালি সুখ আর সুখ"]

#tokenizing the data
checkpoint = 'buetcsenlp/banglabert'
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

tokenize = tokenizer(sentences,padding = True,trucnation = True,return_tensors = 'pt')

#create the model

model = AutoModel.from_pretrained(checkpoint)


#see the hidden state
output = model(sentences)
print(output.last_hidden_state.shape)  #it will give 3 information: 1)batch_size(2 in this case),sequence length(6 words),vector no(768 or more;this is neuron probably)
