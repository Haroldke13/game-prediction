from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = "deepseek-ai/DeepSeek-R1"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

def predict_match_outcome(match_data):
    """Generate a prediction for a soccer match based on scraped data using DeepSeek-R1."""
    prompt = f"Based on the following data: {match_data}, predict the outcome of the game."

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate output
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=50)

    # Decode response
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return prediction.strip()
