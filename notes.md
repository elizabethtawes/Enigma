Notes on PyEnigma

## Building The Enigma
* rotors can either be a space separated list of rotor names, or a list of rotor
name strings. For a complete list of supported rotor names, see Simulated rotor
models (http://py-enigma.readthedocs.io/en/latest/reference.html#rotor-table-label).

* reflector is a string that names the reflector to use. For a complete list of
supported reflector names, see Simulated reflector types (http://py-enigma.readthedocs.io/en/latest/reference.html#reflector-table-label).

* ring_settings can be a space separated list of uppercase letters or numbers,
as would be found on a key sheet. An empty string or None means ring settings
of all ‘A’ or 1.

* plugboard_settings can either be space separated uppercase letter pairs, or
slash separated numbers. Note that ‘AB’ is equivalent to ‘1/2’, etc.

* in order to create an enigma machine from a monthly key sheet, use key file format
(http://py-enigma.readthedocs.io/en/latest/keyfile.html)

## Encrypting and Decrypting
* first set initial rotor positions

* to check current rotor positions use get_display method: machine.get_display()

* to simulate one key entry use key_press method: machine.key_press('A')

* to simulate a string entry use process_text method:
    machine.process_text('This is a test', replace_char='X')
