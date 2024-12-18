import binascii
import hashlib
import base58
from ecdsa import SECP256k1, SigningKey
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

def process_key(i):
    try:
        private_key = i.to_bytes(32, byteorder='big')
        sk = SigningKey.from_string(private_key, curve=SECP256k1)
        vk = sk.verifying_key
        compressed_public_key = vk.to_string('compressed')
        compressed_public_key_hash = hashlib.new('ripemd160', hashlib.sha256(compressed_public_key).digest()).digest()
        versioned_compressed_public_key_hash = b'\x00' + compressed_public_key_hash
        base58check_encoded_public_key_hash = base58.b58encode_check(versioned_compressed_public_key_hash).decode('utf-8')
        wif_private_key = b'\x80' + private_key
        wif_checksum = hashlib.sha256(hashlib.sha256(wif_private_key).digest()).digest()[:4]
        wif_encoded_private_key = base58.b58encode(wif_private_key + wif_checksum).decode('utf-8')

        desired_value = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
        if base58check_encoded_public_key_hash == desired_value:
            matching_key_info = f"Private Key (Decimal): {i}\n" \
                                f"Private Key (Hexadecimal): {binascii.hexlify(private_key).decode('utf-8')}\n" \
                                f"WIF Private Key: {wif_encoded_private_key}\n" \
                                f"Base58Check Encoded Public Key Hash: {base58check_encoded_public_key_hash}\n"
            with open("matching_keys.txt", "a") as file:
                file.write(matching_key_info + "\n")
            return matching_key_info
    except Exception as e:
        return f"Error processing key {i}: {e}"

def main():
    start = 46346217550346035726
    end = 46346217550346735726
    num_processes = min(8, cpu_count())  # Limit to 2 processes for slower CPUs

    with open("matching_keys.txt", "w") as file:
        file.write("Matching Private Keys, WIFs, and Public Key Hashes:\n")

    chunk_size = 10  # Smaller chunks for reduced memory usage and better responsiveness
    with Pool(processes=num_processes) as pool:
        for result in tqdm(pool.imap_unordered(process_key, range(start, end + 1), chunksize=chunk_size),
                           total=(end - start + 1), desc="Processing Keys"):
            if result and "Error" not in result:
                print(result)

if __name__ == "__main__":
    main()

