# Q1 - Regex Solutions

1. **U.S. ZIP Codes**
```regex
\b\d{5}(?:[- ]\d{4})?\b
```

2. **Words not starting with a capital letter**
```regex
\b(?![A-Z])[A-Za-z][A-Za-z'-]*\b
```

3. **Numbers with optional sign, commas, decimal, scientific notation**
```regex
[+-]?\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:[eE][+-]?\d+)?
```

4. **Spelling variants of "email" (case-insensitive, with space/hyphen/en-dash)**
```regex
(?i)\be[\s\-–]?mail\b
```

5. **go, goo, gooo… with optional punctuation**
```regex
\bgo+[\!\.\,\?]?\b
```

6. **Lines ending with question mark + optional closing quotes/brackets**
```regex
\?[)"'\]\s]*$
```