# Easy-Bitcoin-puzzle-key-scanner
a easy private key scanner CPU script that when it detects a specified wallet between a range of private keys ... it will save the wallet info to a txt file....... no backdoors , it can run even offline
____________________________________________________________________________________________________________________________________
Please consider donating if you like my script . I'm a 17 yo europoor kid from a 3rd world country and this is my first coding attempt 

BTC: 1DibZfR2BCQyPDLvcuiWRMsdyUDwFEtV1
____________________________________________________________________________________________________________________________________





Requirements:

    you will need python 3.13 , then in powershell:  pip install binascii , hashlib , base58 , tqdm , ecdsa .

    you will also need IDLE 3.13 if it doesnt come with your python


How to USE:

    Easy to use, all you have to do is right click the script and edit the [ desired_value = "wallet your are searching for" ] its automatically set to search for puzzle #67

    then edit the def main():    
    start = "start private key range in DECIMAL"
    end = "end private key range in DECIMAL"  ]   this setting is also automatically set to scan trough 40000000000000000:7ffffffffffffffff , the wallet is somewhere in that range 
    
    edit your desired values 
    
you need to convert your private key from HEX to DEC , this script only works with decimals .. for example "hex: 40000000000000000 is converted to dec: 73786976294838206464"
    
i use this website to convert hex to dec : https://www.binaryhexconverter.com/hex-to-decimal-converter

After you selected your desired search range , you just save and double click the script and it will scan trough the selected range of private keys and if the lucky wallet is there, it will be printed in the matching_keys.txt . no backdoors , no stealing your findings . this script runs even in offline mode. 

If u find this helpfull and want to support me in creating better scripts , please consider donating  BTC : 1DibZfR2BCQyPDLvcuiWRMsdyUDwFEtV1

Thank you 

   PS: i also uploaded a test for puzzle 66 to see how it works 
