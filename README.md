# Terraform code to deploy three-tier architecture on azure

## Resources to be deployed

1. virtual network with three subnets.
2. Each subnet will have one virtual machine.
3. Web virtual machine -> allow inbound traffic from internet only.
4. App virtual machine -> allow traffic from Web virtual machine only and can reply the same virtual machine again.
5. App can connect to database and database can connect to app but database cannot connect to web.


### The Terraform resources will consists of following structure

```
├── main.tf                   // The primary entrypoint for terraform resources.
├── vars.tf                   // It contain the declarations for variables.
├── output.tf                 // It contain the declarations for outputs.
├── terraform.tfvars          // The file to pass the terraform variables values.
```

### Module

Below are the five modules used to create the 3-tier Architecture:
1. resourcegroup - creating resourcegroup
2. networking - creating azure virtual network and required subnets
3. securitygroup - creating network security group, setting desired security rules and associating them to subnets
4. compute - creating availability sets, network interfaces and virtual machines
5. database - creating database server and database

All the stacks are placed in the modules folder and the variable are stored under **terraform.tfvars**


## Deployment

### Steps

**Step 1** `terraform init`

**Step 2** `terraform plan`

**Step 3** `terraform validate`

**Step 4** `terraform apply`
