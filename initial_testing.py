from enigma.machine import EnigmaMachine

# setup machine according to specs from a daily key sheet:
# note this simulates army or air force machines
machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',
    reflector='B',
    ring_settings=[1,20,11],
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
    )

# use settings like this to simulate navy machines
# machine_navy = EnigmaMachine.from_key_sheet(
#     rotors='Beta VII IV V',
#     reflector='B-Thin',
#     ring_settings='G N O',
#     plugboard_settings='18/26 17/4 21/6 3/16 19/14 22/7 8/1 12/25 5/9 10/15'
# )

# set machine initial starting position
machine.set_display('WXC')

# decrypt the message key
msg_key = machine.process_text('KCH')

# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)

ciphertext = 'NIBLFMYMLLUFWCASCSSNVHAZ'
plaintext = machine.process_text(ciphertext)

print(plaintext)
