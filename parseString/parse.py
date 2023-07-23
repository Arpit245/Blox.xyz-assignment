from decimal import Decimal

def custom_json(input_string):
    index = 0  

    def skip_space():
        nonlocal index
        while index < len(input_string) and input_string[index].isspace():
            index += 1

    def parse_content():
        nonlocal index
        skip_space()

        if index >= len(input_string):
            return None

        current_char = input_string[index]

        if current_char == '{':
            return parse_object()
        elif current_char == '[':
            return parse_array()
        elif current_char == '"':
            return parse_string()
        elif current_char.isdigit() or current_char in '+-':
            return parse_digits()
        elif current_char == 't' or current_char == 'f':
            return parse_boolean()
        elif current_char == 'n':
            return parse_null()

    def parse_object():
        nonlocal index
        obj = {}

        skip_space()
        if index >= len(input_string) or input_string[index] != '{':
            return obj

       
        index += 1

        while index < len(input_string) and input_string[index] != '}':
            skip_space()
            key = parse_string()

            skip_space()
            if index >= len(input_string) or input_string[index] != ':':
                break

       
            index += 1

            value = parse_content()
            obj[key] = value

            skip_space()
            if index < len(input_string) and input_string[index] == ',':
                index += 1

      
        skip_space()
        if index < len(input_string) and input_string[index] == '}':
            index += 1

        return obj

    def parse_string():
        nonlocal index
        value = ''
        index += 1

        while index < len(input_string) and input_string[index] != '"':
            value += input_string[index]
            index += 1

    
        if index < len(input_string) and input_string[index] == '"':
            index += 1

        return value

    def parse_array():
        nonlocal index
        arr = []

        skip_space()
        if index >= len(input_string) or input_string[index] != '[':
            return arr

        index += 1

        while index < len(input_string) and input_string[index] != ']':
            value = parse_content()
            arr.append(value)

           
            skip_space()
            if index < len(input_string) and input_string[index] == ',':
                index += 1

    
        skip_space()
        if index < len(input_string) and input_string[index] == ']':
            index += 1

        return arr

    def parse_boolean():
        nonlocal index
        c = input_string[index:index+4]
        index += 4
        return c == 'true'

    def parse_null():
        nonlocal index
        index += 4
        return None

    def parse_digits():
        nonlocal index
        num = ''
        valid_chars = '+-0123456789.eE'

        while index < len(input_string) and input_string[index] in valid_chars:
            num += input_string[index]
            index += 1

        if '.' in num or 'e' in num.lower():
           
            return Decimal(num)
        else:
           
            return int(num)

    return parse_content()


input_string = '{"name": "Arpit", "age": 24, "weight": "60", "is_student": true, "address": null, "marks": [90, 85, 95]}'
parsed_object = custom_json(input_string)
print(parsed_object)
