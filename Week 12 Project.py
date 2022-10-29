# AWS services List

#1. The list should be empty intially.

List = []

#2. Populate the list using append or insert. 

List.append('ECS')
List.append('DynamoDB')
List.append('EC2')
List.append('CloudFront')
List.append('S3')
List.append('CloudWatch')
List.append('RDS')
List.append('CloudFormation')


#3. Print the list and the length of the list.

print('8 Must Have AWS Services:', List)
List_length = str(len(List))

#4. Remove two specific services from the list by name or by index.  

del List [0:-1]
print('6 Must Have AWS Services:', List)

#5. Print the new list and the new length of the list.

List_length = str(len(List))
print('Available Services:', List_length)
