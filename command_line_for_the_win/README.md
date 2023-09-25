# Secure File Transfer using SFTP

This guide provides step-by-step instructions on how to securely transfer files using the Secure File Transfer Protocol (SFTP). SFTP is a secure method for transferring files between your local machine and a remote server. In this guide, we'll cover the following steps:

1. **Take Screenshots**:
   - Take screenshots of the completed levels as mentioned in the general requirements. Ensure that these screenshots are saved on your local machine.

2. **Open Terminal or Command Prompt**:
   - Open a terminal or command prompt on your local machine. The exact method for doing this may vary depending on your operating system (e.g., macOS, Linux, Windows).

3. **Establish an SFTP Connection**:
   - Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the following information:
     - **Hostname**: The hostname or IP address of the remote server.
     - **Username**: Your username for accessing the remote server.
     - **Password**: Your password for authenticating with the remote server.

     Usage: sftp <Username>@<Hostname>
           Enter the password when prompted.

4. **Navigate to the Directory**:
   - Once connected, navigate to the directory on the remote server where you want to upload the screenshots. Use the `cd` command to change directories.

5. **Upload Screenshots**:
   - Use the SFTP `put` command to upload the screenshots from your local machine to the remote server. Make sure to specify the correct local and remote file paths.
   
    Usage: put /Users/edgarkebiro/Desktop/0-first_9_tasks.png

6. **Confirm Transfer**:
   - After uploading, confirm that the screenshots have been successfully transferred by checking the remote directory. You can use SFTP commands or remote file system tools to verify the presence of the files.

7. **Push Screenshots to GitHub**:
   - Once the screenshots are successfully transferred to the remote server, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.

8. **Include Instructions in README.md**:
   - In your project's README.md file, include detailed instructions on how you performed the file transfer using SFTP. This will help reviewers understand the process and reproduce it if needed.

9. **Note on Screenshot Directory**:
   - Ensure that the screenshots of completed levels are located inside the directory specified in the note: `/root/alx-system_engineering-devops/command_line_for_the_win/`.

By following these steps, you can securely transfer files from your local machine to a remote server using SFTP and document the process for your project
