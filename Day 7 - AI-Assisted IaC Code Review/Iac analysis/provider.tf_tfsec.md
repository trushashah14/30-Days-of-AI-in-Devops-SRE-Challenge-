# tfsec Analysis for ../../..\IT\AWS Architecture using Terraform\provider.tf


[0m[3mResult #1[0m [0m[1m[31mCRITICAL[39m[0m[39m[0m [1mSecurity group rule allows ingress from public internet.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:12
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m    3  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"alb_sg"[0m {[0m
[0m[90m    .  [0m
[0m[31m   12  [0m[0m[31m[[39m[0m[0m [0m    [38;5;245mcidr_blocks[0m = [[38;5;37m"0.0.0.0/0"[0m][38;5;239m        // Accept from any IP (public internet)[0m
[0m[90m   ..  [0m
[0m[90m   25  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-no-public-ingress-sgr
[0m[0m  [2m    Impact[0m Your port exposed to the internet
[0m[0m  [2mResolution[0m Set a more restrictive cidr range
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/no-public-ingress-sgr/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule#cidr_blocks[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #2[0m [0m[1m[31mCRITICAL[39m[0m[39m[0m [1mSecurity group rule allows egress to multiple public internet addresses.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:19
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m    3  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"alb_sg"[0m {[0m
[0m[90m    .  [0m
[0m[31m   19  [0m[0m[31m[[39m[0m[0m [0m    [38;5;245mcidr_blocks[0m = [[38;5;37m"0.0.0.0/0"[0m][0m
[0m[90m   ..  [0m
[0m[90m   25  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-no-public-egress-sgr
[0m[0m  [2m    Impact[0m Your port is egressing data to the internet
[0m[0m  [2mResolution[0m Set a more restrictive cidr range
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/no-public-egress-sgr/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #3[0m [0m[1m[31mCRITICAL[39m[0m[39m[0m [1mSecurity group rule allows egress to multiple public internet addresses.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:44
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m   28  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"ec2_sg"[0m {[0m
[0m[90m   ..  [0m
[0m[31m   44  [0m[0m[31m[[39m[0m[0m [0m    [38;5;245mcidr_blocks[0m = [[38;5;37m"0.0.0.0/0"[0m][0m
[0m[90m   ..  [0m
[0m[90m   50  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-no-public-egress-sgr
[0m[0m  [2m    Impact[0m Your port is egressing data to the internet
[0m[0m  [2mResolution[0m Set a more restrictive cidr range
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/no-public-egress-sgr/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #4[0m [0m[1m[31mCRITICAL[39m[0m[39m[0m [1mListener for application load balancer does not use HTTPS.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[3m[2m:78
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m   75  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_lb_listener"[0m [38;5;37m"alb_listener"[0m {[0m
[0m[90m   ..  [0m
[0m[31m   78  [0m[0m[31m[[39m[0m[0m [0m  [38;5;245mprotocol[0m          = [38;5;37m"HTTP"[0m[0m [3m[2m[3m("HTTP")[0m
[0m[90m   ..  [0m
[0m[90m   86  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-elb-http-not-used
[0m[0m  [2m    Impact[0m Your traffic is not protected
[0m[0m  [2mResolution[0m Switch to HTTPS to benefit from TLS security features
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/elb/http-not-used/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_listener[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #5[0m [0m[31mHIGH[39m[0m [1mApplication load balancer is not set to drop invalid headers.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:54-61
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m   54  [0m[0m [0m[0m [0m[38;5;33mresource[0m [38;5;37m"aws_lb"[0m [38;5;37m"app_lb"[0m {[0m
[0m[31m   55  [0m[0m [0m[0m   [38;5;245mname[0m               = [38;5;37m"aws-prod-app-lb"[0m
[0m[31m   56  [0m[0m [0m[0m [0m  [38;5;245mload_balancer_type[0m = [38;5;37m"application"[0m[38;5;239m              // HTTP/HTTPS load balancing (Layer 7)[0m
[0m[31m   57  [0m[0m [0m[0m [0m  [38;5;245minternal[0m           = [38;5;166mfalse[0m[38;5;239m                      // Not internal; exposed to the internet[0m
[0m[31m   58  [0m[0m [0m[0m [0m  [38;5;245msecurity_groups[0m    = [aws_security_group.alb_sg.id][0m
[0m[31m   59  [0m[0m [0m[0m   [38;5;245msubnets[0m            = aws_subnet.public_subnet[[38;5;245m*[0m].id[0m
[0m[31m   60  [0m[0m [0m[0m   [38;5;245mdepends_on[0m         = [aws_internet_gateway.igw_vpc][38;5;239m  // Ensure IGW exists before LB[0m
[0m[31m   61  [0m[0m [0m[0m [0m}[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-elb-drop-invalid-headers
[0m[0m  [2m    Impact[0m Invalid headers being passed through to the target of the load balance may exploit vulnerabilities
[0m[0m  [2mResolution[0m Set drop_invalid_header_fields to true
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/elb/drop-invalid-headers/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb#drop_invalid_header_fields[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #6[0m [0m[31mHIGH[39m[0m [1mLoad balancer is exposed publicly.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:57
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m   54  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_lb"[0m [38;5;37m"app_lb"[0m {[0m
[0m[90m   55  [0m[0m    [38;5;245mname[0m               = [38;5;37m"aws-prod-app-lb"[0m
[0m[90m   56  [0m[0m  [0m  [38;5;245mload_balancer_type[0m = [38;5;37m"application"[0m[38;5;239m              // HTTP/HTTPS load balancing (Layer 7)[0m
[0m[31m   57  [0m[0m[31m[[39m[0m[0m [0m  [38;5;245minternal[0m           = [38;5;166mfalse[0m[38;5;239m                      // Not internal; exposed to the internet[0m[0m [3m[2m[3m(false)[0m
[0m[90m   58  [0m[0m  [0m  [38;5;245msecurity_groups[0m    = [aws_security_group.alb_sg.id][0m
[0m[90m   59  [0m[0m    [38;5;245msubnets[0m            = aws_subnet.public_subnet[[38;5;245m*[0m].id[0m
[0m[90m   60  [0m[0m    [38;5;245mdepends_on[0m         = [aws_internet_gateway.igw_vpc][38;5;239m  // Ensure IGW exists before LB[0m
[0m[90m   61  [0m[0m  [0m}[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-elb-alb-not-public
[0m[0m  [2m    Impact[0m The load balancer is exposed on the internet
[0m[0m  [2mResolution[0m Switch to an internal load balancer or add a tfsec ignore
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/elb/alb-not-public/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #7[0m [0m[31mHIGH[39m[0m [1mLaunch template does not require IMDS access to require a token[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:90-109
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m   90  [0m[0m[31m┌[39m[0m[0m [0m[38;5;33mresource[0m [38;5;37m"aws_launch_template"[0m [38;5;37m"ec2_launch_template"[0m {[0m
[0m[31m   91  [0m[0m[31m│[39m[0m[0m   [38;5;245mname[0m = [38;5;37m"aws-prod-web-server"[0m
[0m[31m   92  [0m[0m[31m│[39m[0m[0m [0m[0m
[0m[31m   93  [0m[0m[31m│[39m[0m[0m   [38;5;245mimage_id[0m      = [38;5;37m"ami-014e30c8a36252ae5"[0m[38;5;239m          // Custom AMI ID (Ubuntu or app image)[0m
[0m[31m   94  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245minstance_type[0m = [38;5;37m"t2.micro"[0m[38;5;239m                       // Free-tier eligible[0m
[0m[31m   95  [0m[0m[31m│[39m[0m[0m [0m
[0m[31m   96  [0m[0m[31m│[39m[0m[0m [0m  network_interfaces {[0m
[0m[31m   97  [0m[0m[31m│[39m[0m[0m     [38;5;245massociate_public_ip_address[0m = [38;5;166mfalse[0m[38;5;239m            // Instance stays in private subnet[0m
[0m[31m   98  [0m[0m[31m└[39m[0m[0m [0m    [38;5;245msecurity_groups[0m             = [aws_security_group.ec2_sg.id][0m
[0m[90m   ..  [0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-enforce-launch-config-http-token-imds
[0m[0m  [2m    Impact[0m Instance metadata service can be interacted with freely
[0m[0m  [2mResolution[0m Enable HTTP token requirement for IMDS
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/enforce-launch-config-http-token-imds/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#metadata-options[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #8[0m [0m[33mMEDIUM[39m[0m [1mVPC Flow Logs is not enabled for VPC [0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\vpc.tf[2m[3m:2-9
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m    2  [0m[0m [0m[0m [0m[38;5;33mresource[0m [38;5;37m"aws_vpc"[0m [38;5;37m"custom_vpc"[0m {[0m
[0m[31m    3  [0m[0m [0m[0m   [38;5;245mcidr_block[0m           = [38;5;37m"10.0.0.0/16"[0m[38;5;239m              // Primary CIDR block for the VPC, allows 65,536 IPs[0m
[0m[31m    4  [0m[0m [0m[0m [0m  [38;5;245menable_dns_support[0m   = [38;5;166mtrue[0m[38;5;239m                       // Enables internal DNS resolution within the VPC[0m
[0m[31m    5  [0m[0m [0m[0m [0m  [38;5;245menable_dns_hostnames[0m = [38;5;166mtrue[0m[38;5;239m                       // Assigns DNS hostnames to instances for easy access[0m
[0m[31m    6  [0m[0m [0m[0m [0m  [38;5;245mtags[0m = {[0m
[0m[31m    7  [0m[0m [0m[0m     [38;5;245mName[0m = [38;5;37m"aws-prod"[0m[38;5;239m                                 // Tags the VPC resource for identification in the console[0m
[0m[31m    8  [0m[0m [0m[0m [0m  }[0m
[0m[31m    9  [0m[0m [0m[0m }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-require-vpc-flow-logs-for-all-vpcs
[0m[0m  [2m    Impact[0m Without VPC flow logs, you risk not having enough information about network traffic flow to investigate incidents or identify security issues.
[0m[0m  [2mResolution[0m Enable flow logs for VPC
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/require-vpc-flow-logs-for-all-vpcs/[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #9[0m [0m[97mLOW[39m[0m [1mSecurity group rule does not have a description.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:15-20
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m    3  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"alb_sg"[0m {[0m
[0m[90m    .  [0m
[0m[31m   15  [0m[0m[31m┌[39m[0m[0m   egress {[0m
[0m[31m   16  [0m[0m[31m│[39m[0m[0m     [38;5;245mfrom_port[0m   = [38;5;37m0[0m[38;5;239m                    // Allow all outbound traffic[0m
[0m[31m   17  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mto_port[0m     = [38;5;37m0[0m
[0m[31m   18  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mprotocol[0m    = [38;5;37m"-1"[0m[38;5;239m                 // "-1" means all protocols[0m
[0m[31m   19  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mcidr_blocks[0m = [[38;5;37m"0.0.0.0/0"[0m][0m
[0m[31m   20  [0m[0m[31m└[39m[0m[0m   }[0m
[0m[90m   ..  [0m
[0m[90m   25  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-add-description-to-security-group-rule
[0m[0m  [2m    Impact[0m Descriptions provide context for the firewall rule reasons
[0m[0m  [2mResolution[0m Add descriptions for all security groups rules
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/add-description-to-security-group-rule/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #10[0m [0m[97mLOW[39m[0m [1mSecurity group rule does not have a description.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:33-38
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m   28  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"ec2_sg"[0m {[0m
[0m[90m   ..  [0m
[0m[31m   33  [0m[0m[31m┌[39m[0m[0m   ingress {[0m
[0m[31m   34  [0m[0m[31m│[39m[0m[0m     [38;5;245mfrom_port[0m       = [38;5;37m0[0m[38;5;239m               // Allow incoming traffic on all ports[0m
[0m[31m   35  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mto_port[0m         = [38;5;37m0[0m
[0m[31m   36  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mprotocol[0m        = [38;5;37m"-1"[0m[38;5;239m            // All protocols allowed[0m
[0m[31m   37  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245msecurity_groups[0m = [aws_security_group.alb_sg.id][38;5;239m  // Only from ALB SG[0m
[0m[31m   38  [0m[0m[31m└[39m[0m[0m [0m  }[0m
[0m[90m   ..  [0m
[0m[90m   50  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-add-description-to-security-group-rule
[0m[0m  [2m    Impact[0m Descriptions provide context for the firewall rule reasons
[0m[0m  [2mResolution[0m Add descriptions for all security groups rules
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/add-description-to-security-group-rule/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #11[0m [0m[97mLOW[39m[0m [1mSecurity group rule does not have a description.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:40-45
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m   28  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"ec2_sg"[0m {[0m
[0m[90m   ..  [0m
[0m[31m   40  [0m[0m[31m┌[39m[0m[0m   egress {[0m
[0m[31m   41  [0m[0m[31m│[39m[0m[0m     [38;5;245mfrom_port[0m   = [38;5;37m0[0m[38;5;239m                   // Allow all outbound traffic[0m
[0m[31m   42  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mto_port[0m     = [38;5;37m0[0m
[0m[31m   43  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mprotocol[0m    = [38;5;37m"-1"[0m
[0m[31m   44  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mcidr_blocks[0m = [[38;5;37m"0.0.0.0/0"[0m][0m
[0m[31m   45  [0m[0m[31m└[39m[0m[0m   }[0m
[0m[90m   ..  [0m
[0m[90m   50  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-add-description-to-security-group-rule
[0m[0m  [2m    Impact[0m Descriptions provide context for the firewall rule reasons
[0m[0m  [2mResolution[0m Add descriptions for all security groups rules
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/add-description-to-security-group-rule/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #12[0m [0m[97mLOW[39m[0m [1mSecurity group rule does not have a description.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\AWS Architecture using Terraform\sg_asg_alb.tf[2m[3m:8-13
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m    3  [0m[0m  [0m[38;5;33mresource[0m [38;5;37m"aws_security_group"[0m [38;5;37m"alb_sg"[0m {[0m
[0m[90m    .  [0m
[0m[31m    8  [0m[0m[31m┌[39m[0m[0m   ingress {[0m
[0m[31m    9  [0m[0m[31m│[39m[0m[0m     [38;5;245mfrom_port[0m   = [38;5;37m80[0m[38;5;239m                   // Allow incoming traffic on port 80 (HTTP)[0m
[0m[31m   10  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mto_port[0m     = [38;5;37m80[0m
[0m[31m   11  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mprotocol[0m    = [38;5;37m"tcp"[0m
[0m[31m   12  [0m[0m[31m│[39m[0m[0m [0m    [38;5;245mcidr_blocks[0m = [[38;5;37m"0.0.0.0/0"[0m][38;5;239m        // Accept from any IP (public internet)[0m
[0m[31m   13  [0m[0m[31m└[39m[0m[0m [0m  }[0m
[0m[90m   ..  [0m
[0m[90m   25  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-ec2-add-description-to-security-group-rule
[0m[0m  [2m    Impact[0m Descriptions provide context for the firewall rule reasons
[0m[0m  [2mResolution[0m Add descriptions for all security groups rules
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/ec2/add-description-to-security-group-rule/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m  [1mtimings[0m
  ──────────────────────────────────────────
[0m[0m  [2mdisk i/o            [0m 4.5085ms
[0m[0m  [2mparsing             [0m 12.1457ms
[0m[0m  [2madaptation          [0m 1.8593ms
[0m[0m  [2mchecks              [0m 25.5204ms
[0m[0m  [2mtotal               [0m 44.0339ms
[0m
[0m  [1mcounts[0m
  ──────────────────────────────────────────
[0m[0m  [2mmodules downloaded  [0m 0
[0m[0m  [2mmodules processed   [0m 1
[0m[0m  [2mblocks processed    [0m 20
[0m[0m  [2mfiles read          [0m 3
[0m
[0m  [1mresults[0m
  ──────────────────────────────────────────
[0m[0m  [2mpassed              [0m 14
[0m[0m  [2mignored             [0m 0
[0m[0m  [2mcritical            [0m 4
[0m[0m  [2mhigh                [0m 3
[0m[0m  [2mmedium              [0m 1
[0m[0m  [2mlow                 [0m 4
[0m
[0m  [31m[1m14 passed, 12 potential problem(s) detected.

[0m