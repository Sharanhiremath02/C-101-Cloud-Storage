import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ayfg1G4EprcE0PDFvcHsgvKfyKmW00-PSs8ezRVrecmANf4XE7JEDtbxryIpm_NtVjKg8HoAIj8MUqTIM91_G8v49Y_MqmEHpSTjrEe9s2AofDtzkz-eThDxlAGWisguWRcOXDY'
    transferData = TransferData(access_token)

    file_from = "test.txt"#input("Enter The Source File Path:")
    file_to =  "/test.txt"#input("Enter The Dropbox Path:") 
    # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Uploaded Successfully")

main()