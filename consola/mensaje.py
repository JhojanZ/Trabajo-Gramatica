import sys

def print_logo_banner():
    print(r'''
    < Hi High-LOGO! >
    ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    ''')

def mensaje_error(error):
    print(rf'''
    //   {error}    \\
    \\ python hlogoc.py inputfile.hlogo //
    -------------------------------------
        \   ^__^ 
        \  (oo)\_______
           (__)\       )\/\\
               ||----w |
               ||     ||
    ''')
    sys.exit(1)
