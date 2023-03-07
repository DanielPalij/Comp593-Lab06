import hashlib
import os
import requests
import subprocess

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    
    sha_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
    resp_msg = requests.get(sha_url)
    
    if resp_msg.status_code == requests.codes.ok:
        real_hash = resp_msg.text
        hash = real_hash.split()[0]

    return hash

def download_installer():
    
    installer_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe'
    resp = requests.get(installer_url)
    
    if resp.status_code == requests.codes.ok:

        installer_data = resp.content

    return installer_data

def installer_ok(installer_data, expected_sha256):
    
    downloaded_hash = hashlib.sha256(installer_data).hexdigest()
    if expected_sha256 == downloaded_hash:
        return True
   
    else:
       
        return False
   


def save_installer(installer_data):
    installer_filename = 'vlc-3.0.18-win64.exe'
    installer_path = os.path.join(os.getenv('TEMP'), installer_filename)
   
    with open(installer_path, 'wb') as file:
        file.write(installer_data)
    
    return installer_path
    
    
    

def run_installer(installer_path):
    
    subprocess.run(["runas", "/user:Administrator", installer_path, '/L=1033', '/S'])
    
    return
    
def delete_installer(installer_path):
    
    os.remove(installer_path)
    
    return

if __name__ == '__main__':
    main()