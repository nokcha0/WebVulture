import re

def extract_types_and_payloads(log_text):
    if isinstance(log_text, list):
        log_text = "\n".join(log_text)

    # Find all occurrences of "Type:" and related payload information
    type_sections = re.split(r'\nType: ', log_text)
    extracted_info = []

    for section in type_sections[1:]:  # Skip the first split since it's before first 'Type'
        type_match = re.match(r'(.*?)\nTitle: (.*?)\nPayload: (.*?)\nVector: (.*)', section, re.DOTALL)
        
        if type_match:
            attack_type = type_match.group(1).strip()
            title = type_match.group(2).strip()
            payload = type_match.group(3).strip()
            vector = type_match.group(4).strip()

            # Process payload by splitting by "&" and extracting key-value pairs
            param_pairs = payload.split('&')
            extracted_params = [f"{param.split('=', 1)[0]}={param.split('=', 1)[1]}" for param in param_pairs if '=' in param]

            extracted_info.append({
                "type": attack_type,
                "title": title,
                "payload": payload,
                "vector": vector,
                "simplified_payload": extracted_params
            })

    return extracted_info

def simplify_payload(log_text):
    # Ensure log_text is a string
    if isinstance(log_text, list):
        log_text = "\n".join(log_text)

    extracted_data = extract_types_and_payloads(log_text)

    formatted_result = []

    # Extract and print exploitable URL
    url_match = re.search(r'Exploitable URL: (.*?)\n', log_text)
    if url_match:
        formatted_result.append(f"Exploitable URL: {url_match.group(1)}\n")

    # Extract and print parameter
    param_match = re.search(r'Parameter: (.*?)\n', log_text)
    if param_match:
        formatted_result.append(f"Parameter: {param_match.group(1)}\n")

    for item in extracted_data:
        formatted_result.append(f"Type: {item['type']}")
        formatted_result.append(f"Title: {item['title']}")
        formatted_result.append(f"Payload: {item['payload']}")
        formatted_result.append(f"Vector: {item['vector']}")
        formatted_result.append("==============\n")
        formatted_result.append("Simplified Payload:")
        formatted_result.extend(item["simplified_payload"])

    return formatted_result 
