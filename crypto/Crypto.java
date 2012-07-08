import javax.crypto.*;
import javax.crypto.spec.*;
import java.io.*;


public class Crypto {
    
    static String getStringFromFile(String filepath) {
	StringBuffer buffer = new StringBuffer();
	try {
	    FileInputStream fis = new FileInputStream(filepath);
	    InputStreamReader isr = new InputStreamReader(fis, "UTF8");
	    Reader in = new BufferedReader(isr);
	    int ch;

	    while ((ch = in.read()) > -1) {
		buffer.append((char)ch);
	    }

	    in.close();
	    return buffer.toString();
	} catch (IOException e) {
	    e.printStackTrace();
	    return null;
	}
    }
    
    
    public static String byteArrayToHexString (byte buf[]) {
	StringBuffer strbuf = new StringBuffer(buf.length * 2);
	int i;
	
	for (i = 0; i < buf.length; i++) {
	    if (((int) buf[i] & 0xff) < 0x10) {
		strbuf.append("0");
	    }
	    strbuf.append(Long.toString((int) buf[i] & 0xff, 16));
	}
	
	return strbuf.toString();
    }
    
    
    public static byte[] hexStringToByteArray(String s) {
	int len = s.length();
	byte[] data = new byte[len / 2];

	for (int i = 0; i < len; i += 2) {
	    data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i+1), 16));
	}

	return data;
    }
    
    
    public static String encrypt_text(String text, String secret_key_str) throws Exception {
	// Get bytes from strings
	byte[] input_bytes = text.getBytes();
	byte[] key_bytes = secret_key_str.getBytes();
	
	// Generate the key for encryption		
	SecretKeySpec secret_key = new SecretKeySpec(key_bytes, "AES");
	
	// Instantiate the cipher
	Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
	cipher.init(Cipher.ENCRYPT_MODE, secret_key);
	
	// Encrypt the input string
	byte[] encrypted_bytes = cipher.doFinal(input_bytes);
	
	// Encode hex
	String encrypted_string = byteArrayToHexString(encrypted_bytes);
	
	return encrypted_string;
    }
    
    
    public static String try_to_decrypt_text(String text, String secret_key_str) throws Exception {
	// Generate the key for encryption		
	byte[] key_bytes = secret_key_str.getBytes();
	SecretKeySpec secret_key = new SecretKeySpec(key_bytes, "AES");
	
	// Instantiate the cipher
	Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
	
	// Initialize the cipher for decryption
	cipher.init(Cipher.DECRYPT_MODE, secret_key);
	
	// Get bytes from string
	byte[] encrypted_bytes = hexStringToByteArray(text);
	
	// Decrypt encrypted string
	byte[] decrypted_bytes = cipher.doFinal(encrypted_bytes);
	
	// Get string form bytes
	String decrypted_string = new String(decrypted_bytes);
	
	return decrypted_string;
    }
    
    
    public static void main(String[] args) throws Exception {
	// Set input msg
	String original_text = new String("this is some text");
	
	// Call encryption and decryption methods
	String encrypted_text = encrypt_text(original_text, new String("key1key1key1key1"));
	String decrypted_text = try_to_decrypt_text(encrypted_text, new String("key1key1key1key1"));
	
	// Print results
	System.out.println("Original text: " + original_text);
	System.out.println("Encrypted text: " + encrypted_text);
	System.out.println("Decrypted text: " + decrypted_text);
	
	// Throw exception if original string and decrypted string do not match
	if (!original_text.equals(decrypted_text)) {
	    throw new Exception("Original string and decrypted string differ.");
	}
    }
}
