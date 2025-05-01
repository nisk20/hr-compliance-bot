from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "microsoft/phi-2"

# Load tokenizer and model (will auto-authenticate)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Run a quick test
inputs = tokenizer("What are my rights if I face harassment at work?", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
