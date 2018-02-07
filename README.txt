This is a demo of flask, ansisble, and deployment on ec2.

To install this demo on EC2 you need the following:

1. An account on Amazon EC2 with access key, and secret key.

2. Set up boto sudo pip install boto boto3, with boto set up the following:
   
   [Credentials]
   aws_access_key=<aws_access_key>
   aws_secret_access_key=<aws_secret_acess_key>

3. Setup ansible:

    sudo pip isntall ansible

4. To enable a second user to login to the EC2 instance. Create a file called
   "ssh.key" in roles/common/files, that has the contents of your ssh key.

5. Update the ansible.cfg with the path to your EC2 key.

6. To deploy on Amazon EC2:

    cd deploy
    ansible-playbook -i hosts site.yaml
