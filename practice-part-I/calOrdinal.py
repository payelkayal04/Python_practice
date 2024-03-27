def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
