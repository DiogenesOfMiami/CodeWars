# def rgb(r, g, b):
#     '''
#     Converts RGB to Hexadecimal Color
#     '''
#     def dec_hex(dec):
#         '''
#         Converts Decimal to Hexadecimal
#         '''
        
#         return hex(dec).lstrip("0x")
        
#     return str(dec_hex(r))+str(dec_hex(g))+str(dec_hex(b))

def rgb(r, g, b):
    '''
    Converts RGB to Hexadecimal Color
    '''
    def dec_hex(dec):
        '''
        Converts Decimal to Hexadecimal
        '''
        if dec>255:
            return 'FF'
        elif dec<=0:
            return '00'
        else:
            return_s = str(hex(dec).lstrip("0x"))
            if len(return_s) > 1:
                return return_s
            else:
                return '0'+return_s
        
    return (dec_hex(r)+dec_hex(g)+dec_hex(b)).upper()
        
print(rgb(255, 255, 255))
print("FFFFFF Expected")
print(rgb(255, 255, 300))
print("FFFFFF Expected")
print(rgb(0,0,0))
print("000000 Expected")
print(rgb(148, 0, 211))
print("9400D3 Expected")
print(rgb(1,2,3))
print("010203 Expected")