from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Load the model and tokenizer from the specified directory
save_directory = "E:\Data\DeathMetal64\GPT - Neo"  # Replace with the directory path where you saved the model and tokenizer
model = GPTNeoForCausalLM.from_pretrained(save_directory)
tokenizer = GPT2Tokenizer.from_pretrained(save_directory)

# Add a padding token to the tokenizer
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

prompt = ''

def get_prompt(content):
    global prompt
    prompt = str(content)

def get_response(content):
    # Tokenize the prompt and get input IDs and attention mask
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    # Generate response using the model
    gen_tokens = model.generate(
        input_ids,
        attention_mask=attention_mask,  # Pass the attention mask to the model
        do_sample=True,
        temperature=0.5,
        max_length=1000000,
    )
    return tokenizer.batch_decode(gen_tokens)[0]
