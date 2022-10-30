def format_name(fname, lname):
    if fname == '' or lname == '':
        return 'You didnt provide valid inputs'
    formated_fname = fname.title()
    formated_lname = lname.title()
    return f'{formated_fname} {formated_lname}'


print(format_name('rodrigo', 'PINHEIRO'))