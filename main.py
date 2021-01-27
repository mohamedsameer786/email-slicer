email_id = input ("enter the email_id:").strip()
username = email_id[:email_id.index("@")] 
domainname = email_id[email_id.index("@")+1:]
print ("your username is ",username," ,your domain name is ",domainname)
