import torch.nn as nn
import torch
from dataclasses import dataclass

class rnn(nn.Module):
    def __init__(self,vocab_size,output_size,embedding_dim,hidden_dim,num_layers,dropout):
        super(rnn,self).__init__()
        self.output_size = output_size
        self.num_layers = num_layers
        self.hidden_dim = hidden_dim

        self.embedding = nn.Embedding(vocab_size,embedding_dim)
        self.lstm = nn.LSTM(embedding_dim,hidden_dim,num_layers,dropout=dropout,batch_first=True)
        self.fc = nn.Linear(hidden_dim,output_size)

        self.dropout = nn.Dropout(p=0.2)

    def forward(self,nn_input,hidden):
        batch_size = nn_input.size(0)
        embeds = self.embedding(nn_input)
        lstm_out,hidden = self.lstm(embeds,hidden)
        lstm_out = lstm_out.contiguous().view(-1,self.hidden_dim)
        output = self.dropout(lstm_out)
        output = self.fc(lstm_out)
        output = output.view(batch_size,-1,self.output_size)
        out = output[:,-1]
        return out,hidden
    
    def init_hidden_weights(self,batch_size,gpu_avail):
        weight=next(self.parameters()).data
        if gpu_avail:
            hidden = (weight.new(self.num_layers, batch_size, self.hidden_dim).zero_().cuda(),
            weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda())
        else:
            hidden = (weight.new(self.num_layers, batch_size, self.hidden_dim).zero_(),
            weight.new(self.num_layers, batch_size, self.hidden_dim).zero_())
        
        return hidden

@dataclass
class HyperParams:
    output_size: int 
    vocab_size: int
    epochs: int = 5
    learning_rate: int = 0.001
    embedding_dim: int = 256
    hidden_dim: int = 500
    num_layers: int = 2
    dropout: int = 0.5