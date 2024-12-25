letter = ''' Dear <|Name|>
         You are selected
         <|Date|>'''

print(letter.replace("<|Name|>", "Prince,").replace("<|Date|>", "24August,2024"))