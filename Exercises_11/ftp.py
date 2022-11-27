import ftplib
# Set the path
path = '/mirrors/ubuntu-cdimage/releases/22.04/release'
# What file to download
filename = 'SHA256SUMS'
# Make the connection
ftp = ftplib.FTP("ftp.heanet.ie")
# Anonymous login
ftp.login()
# Change to the correct directory
ftp.cwd(path)
# Retrieve the file
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
# Cleanly exit
ftp.quit()
