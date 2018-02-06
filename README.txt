This is a demo of flask, ansisble, and deployment on ec2.

To install this demo on EC2 you need the following:

1. An account on Amazon EC2 with access key, and secret key.

2. Set up boto sudo pip install boto boto3, with boto set up the following:
   
   [Credentials]
   aws_access_key=<aws_access_key>
   aws_secret_access_key=<aws_secret_acess_key>

3. Setup ansible:

    sudo pip isntall ansible

4. To deploy on Amazon EC2:

    cd deploy
    ansible-playbook -i hosts site.yaml
