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
    
    
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    
    if resp_msg.status_code == requests.codes.ok:
        realhash = resp_msg.text.split()


    
    # Extract text file content from response message
        file_content = resp_msg.text
    
    
    
    return 

def download_installer():
    
    
    
    
    return

def installer_ok(installer_data, expected_sha256):
    
    
    
    
    return

def save_installer(installer_data):
    
    
    
    return

def run_installer(installer_path):
    return
    
def delete_installer(installer_path):
    return

if __name__ == '__main__':
    main()