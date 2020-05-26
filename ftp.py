import ftplib

def ftp_connect():
 while True:
    site_address = input("Please enter FTP address:")
    user=input("enter your user:")
    password=input("enter your password:")
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(site_address,2121)
            ftp.login(user,password)
            print(ftp.getwelcome())
            print("Current Diretory", ftp.pwd())
            ftp.dir()
            print("Valid commad are cd/get/ls/exit/cr/del -ex: get readme.txt")
            ftp_commad(ftp)
            break
    except ftplib.all_errors as e:
        print("Fail connect check your address and crential",e)

def ftp_commad(ftp):
    while True:
        commad=input("Enter a commad:")
        commads=commad.split()
        if commads[0]=='cd': #change derectory
            try:
                ftp.cwd(commads[1])
                print("Diretory of", ftp.pwd())
                ftp.dir()
                print("Current Diretory", ftp.pwd())
            except ftplib.error_perm as e:
                error_code=str(e).split(None,1)
                if error_code[0]=='550':
                    print(error_code[1],'Diretory may not exist or say have permisson to veiw it')
        elif commads[0]=='cr':#Create file
           try:
               # ftp.cwd(commads[1])
                #print('Create of',ftp.pwd())
                ftp.mkd(commads[1])
                print("File create successfull")
           except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                   print(error_code[1], 'Create may not exist or say have permisson to veiw it')
        elif commads[0]=='del':#Delete file
           try:
               # ftp.cwd(commads[1])
                #print('Create of',ftp.pwd())
                ftp.delete(commads[1])
                print("Delete file successfull")
           except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                   print(error_code[1], 'Delete may not exist or say have permisson to veiw it')
        elif commads[0]=='rm':#Delete folder
           try:
                ftp.rmd(commads[1])
                print("Delete folder successfull")
           except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                   print(error_code[1], 'Delete may not exist or say have permisson to veiw it')
        elif commads[0]=='get':# Dowload file
            try:
                ftp.retrbinary('RETR'+commads[1],open(commads[1],'wb').write,1024)
                print("File download successfull")
            except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'Diretory may not exist or say have permisson to veiw it')
        elif commads[0]=='up':#Upload File
            try:
                 ftp.storbinary('STOR '+commads[1],open(commads[1],'rb'))
                 print("File upload successfull")
            except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'Diretory may not exist or say have permisson to veiw it')
        elif commads[0]=='ls':
            print("Diretory of", ftp.pwd())
            ftp.dir()
        elif commads[0]=='exit':
            ftp.quit()
            print("goodbye")
            break
        else:
            print("Invalid commad, try again (Valid options:cd/get/ls/exit")
ftp_connect()