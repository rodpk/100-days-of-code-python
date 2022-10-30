def format_name(fname, lname):
    """Take a first and last name 
    and format it to return the title case version of the name."""
    
    if fname == '' or lname == '':
        return 'You didnt provide valid inputs'
    formated_fname = fname.title()
    formated_lname = lname.title()
    return f'{formated_fname} {formated_lname}'


print(format_name('rodrigo', 'PINHEIRO'))
