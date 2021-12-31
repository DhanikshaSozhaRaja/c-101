import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to): 
        dbx = dropbox.Dropbox(self.access_token) 
        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'WmazxqMSbbgAAAAAAAAAAQf0rdr1hBOv6MUvN2s9LstzxEB3wV7vLV_MdoQPtDh3'
    transferData = TransferData(access_token)
    file_from = input("Enter the file to be transferred--")
    file_to = input("Enter the full path to upload in DropBox--")
    transferData.upload_file(file_from, file_to) 
    print("file has been moved !!!")
main()
